from typing import Any, Optional, Type
from types import TracebackType

from seleniumwire.webdriver import Chrome, ChromeOptions  # type: ignore

from .utils.options import get_options  # type: ignore
from .utils.system import get_canonical_os_name, is_windows  # type: ignore


class ChromeLauncher:
    def __init__(self,
        headless: bool = True,
        binary_location: Optional[str] = None,
        download_dir: Optional[str] = None,
        *,
        custom_options: Optional[ChromeOptions] = None,
    ) -> None:
        print(f"Init {self.name}")
        self._chrome_options = custom_options or get_options("chrome", headless, binary_location, download_dir)

    def __enter__(self) -> Chrome:
        chromedriver_path = f"./webdrivers/{get_canonical_os_name()}/chromedriver{'.exe' if is_windows() else ''}"
        self._chrome = Chrome(executable_path=chromedriver_path, options=self._chrome_options)
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
