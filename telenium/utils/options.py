from typing import Literal, Optional, Union

from seleniumwire.webdriver import ChromeOptions, FirefoxOptions  # type: ignore

def get_default_chrome_options() -> ChromeOptions:
    return get_options()

def get_default_firefox_options() -> FirefoxOptions:
    return get_options(option_type="firefox")

def get_options(
        option_type: Literal["chrome", "firefox"] = "chrome",
        headless: bool = True,
        binary_location: Optional[str] = None,
        download_dir: Optional[str] = None,
    ) -> Union[FirefoxOptions, ChromeOptions]:
    options = FirefoxOptions() if option_type == "firefox" else ChromeOptions()

    if headless:
        options.add_argument("--headless")
    
    if binary_location is not None:
        options.binary_location = binary_location
    
    if download_dir is not None:
        prefs = {"download.default_directory": download_dir}
        options.add_experimental_option("prefs", prefs)

    return options
        
