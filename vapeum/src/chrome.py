from pathlib import Path
from typing import Optional, Type
from types import TracebackType
from selenium import webdriver

from .utils.system import get_canonical_os_name, is_windows

class ChromeLauncher:
    def __init__(self,
        headless: bool = True,
        binary_location: Optional[str] = None,
        download_dir: Optional[str] = None,
        *,
        custom_options: Optional[webdriver.ChromeOptions] = None,
    ) -> None:
        print(f"Init {self.name}")
        self._chrome_options = custom_options or webdriver.ChromeOptions()
        if custom_options is None:
            if headless:
                self._chrome_options.add_argument("--headless")
            if binary_location is not None:
                self._chrome_options.binary_location = binary_location
            if download_dir is not None:
                prefs = {"download.default_directory": self._download_dir}
                self._chrome_options.add_experimental_option("prefs", prefs)  

    def __enter__(self) -> webdriver.Chrome:
        chromedriver_path = f"./webdrivers/{get_canonical_os_name()}/chromedriver{'.exe' if is_windows() else ''}"
        self._chrome = webdriver.Chrome(executable_path=chromedriver_path, options=self._chrome_options)
        return self._chrome

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None:
        print(f"Dunder exit {self.name}")
        if exc == None:
            self._chrome.quit()
        else:
            print(f"Error = {exc}")

    @property
    def name(self) -> str:
        return ChromeLauncher.__name__

    @property
    def browser_pid(self) -> int:
        return self._chrome.service.process.pid
    
    @property
    def command_executor_url(self) -> str:
        return self._chrome.command_executor._url
    
    @property
    def session_id(self) -> int:
        return self._chrome.session_id
