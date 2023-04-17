from os import kill
from json import dumps
from signal import SIGTERM
from subprocess import PIPE, Popen
from types import TracebackType
from typing import Dict, Literal, Optional, Type, Union
from contextlib import ExitStack

from selenium import webdriver
from seleniumwire.webdriver import Remote

from .chrome import ChromeLauncher

ENGINE_LAUNCHER_MAPPING = {
    "chrome": ChromeLauncher,
    "firefox": "FirefoxLauncher"
}


class Vapeum: 
    def __init__(
        self,
        engine: Literal["chrome", "firefox"] = "chrome",
        headless: bool = True,
        binary_location: Optional[str] = None,
        download_dir: Optional[str] = None,
        timeout: int = 30,
        *,
        engine_options: Optional[Union[webdriver.ChromeOptions, webdriver.FirefoxOptions]] = None,
        seleniumwire_options: Optional[Dict[str, any]],
    ) -> None:
        self._browser_launcher = ENGINE_LAUNCHER_MAPPING[engine](
            headless,
            binary_location,
            download_dir,
            custom_options=engine_options,
        )
        self._seleniumwire_options = seleniumwire_options
        self._timeout = timeout
        self._exit_stack = ExitStack() 
    
    def __enter__(self) -> Remote:
        self._browser = self._exit_stack.enter_context(self._browser_launcher)
        self._cleanup_pid = self._start_cleanup()
        
        # original executor https://www.linkedin.com/pulse/selenium-how-mount-existing-driver-roei-sabag/?trk=public_profile_article_view
        execute = Remote.execute

        # override newSession command
        def local_executor(self, command, params=None):
            if command != "newSession":
                return execute(self, command, params)
            return {"success": 0, "value": None, 'session_id': self._browser_launcher.session_id}
        
        # mount
        Remote.execute = local_executor
        
        self._controller = Remote(
            command_executor=self._browser_launcher.command_executor_url,
            seleniumwire_options=self._seleniumwire_options,
        )

        # restore orignal functionality
        Remote.execute = execute

        return self._controller

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        if exc is None:
            self._controller.quit()
            kill(self._cleanup_pid, SIGTERM)

    def _start_cleanup(self) -> int:
        process = Popen(
            "python",
            "vapeum/src/utils/_cleanup.py",
            str(self._timeout),
            dumps([self._browser.browser_pid]),
            stdout=PIPE,
            stderr=PIPE,
        )
        return process.pid
