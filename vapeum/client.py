from os import kill
from json import dumps
from signal import SIGTERM
from subprocess import PIPE, Popen
from types import TracebackType
from typing import Any, Dict, Literal, Optional, Type, Union
from contextlib import ExitStack

from seleniumwire.webdriver import ChromeOptions, FirefoxOptions  # type: ignore
from seleniumwire.webdriver import _Remote as WebDriver  # type: ignore

from .chrome import ChromeLauncher  # type: ignore
from .firefox import FirefoxLauncher  # type: ignore
from .utils.logger import logger

BrowserLauncher = Union[Type[ChromeLauncher], Type[FirefoxLauncher]]

ENGINE_LAUNCHER_MAPPING: Dict[str, BrowserLauncher] = {
    "chrome": ChromeLauncher,
    "firefox": FirefoxLauncher,
}

class Vapeum:
    """
    Vapeum is a self-cleaning selenium browser automation tool.
    """ 
    def __init__(
        self,
        timeout: int = 30,
        engine: Literal["chrome", "firefox"] = "chrome",
        headless: bool = True,
        binary_location: Optional[str] = None,
        download_dir: Optional[str] = None,
        *,
        engine_options: Optional[Union[ChromeOptions, FirefoxOptions]] = None,
        seleniumwire_options: Optional[Dict[str, Any]] = None,
    ) -> None:
        self._browser_launcher = ENGINE_LAUNCHER_MAPPING[engine](
            headless,
            binary_location,
            download_dir,
            custom_options=engine_options,
        )
        self._seleniumwire_options: Dict[str, Any] = seleniumwire_options or {}
        self._timeout: int = timeout
        self._exit_stack = ExitStack()
    
    def __enter__(self) -> WebDriver:
        logger.info(f"Entering {self._browser_launcher.name}")
        self._browser = self._exit_stack.enter_context(self._browser_launcher)
        self._cleanup_pid: int = self._start_cleanup()
        logger.info(f"Cleanup pid for {self._browser_launcher.name} is {self._cleanup_pid}")
        return self._browser

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        logger.info(f"Exiting {self._browser_launcher.name}")
        if exc is None:
            logger.info(f"... Quitting browser and killing cleanup process {self._cleanup_pid}")
            self._browser.quit()
            kill(self._cleanup_pid, SIGTERM)

    def _start_cleanup(self) -> int:
        process = Popen(
            [
                "python",
                "vapeum/src/utils/_cleanup.py",
                str(self._timeout),
                dumps([self._browser_launcher.browser_pid])
            ],
            stdout=PIPE,
            stderr=PIPE,
        )
        return process.pid
