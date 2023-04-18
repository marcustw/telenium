from typing import Optional
from seleniumwire.webdriver import ChromeOptions

def get_chrome_options(headless: bool, binary_location: Optional[str], download_dir: Optional[str]) -> ChromeOptions:
    options = ChromeOptions()
    
    if headless:
       options.add_argument("--headless") 
  
    if binary_location is not None:
        options.binary_location = binary_location
    
    if download_dir is not None:
        prefs = {"download.default_directory": download_dir}
        options.add_experimental_option("prefs", prefs)

    return options

def get_default_chrome_options() -> ChromeOptions:
    return get_chrome_options(headless=True)
