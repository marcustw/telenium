# telenium

This is a package for using selenium browser automation tool that is much easier
and requires less configuration. It should fit a typical use case of browser
automation required. There is also auto clean up so you won't have to worry
about the cleaning up.

## Driver Versions

```
ChromeDriver 112.0.5615.49 (bd2a7bcb881c11e8cfe3078709382934e3916914-refs/branch-heads/5615@{#936})
geckodriver 0.33.0 (a80e5fd61076 2023-04-02 18:31 +0000)
```

## Installation

```sh
# pip
pip install telenium

# installing using whl
wget https://github.com/marcustw/telenium/releases/download/v1.0.0/vapeum-1.0-py3-none-any.whl
pip install vapeum-1.0-py3-none-any.whl
```

## Usage

```python
from telenium import Telenium

if __name__ == "__main__":
    telenium = Telenium()
    with telenium as b:
        b.get("https://www.google.com")
        print(f"{b.page_source[:100]}\n")
        for request in b.requests[:2]:
            if request.response:
                print(
                    f"url = {request.url}\nstatus_code = {request.response.status_code}, "
                    "response = {request.response.headers['Content-Type']}\n"
                )

    print("done")
```

## Changelog

- v1.0.1: Renamed from `vapeum` to `telenium` which seems like a better name as
  a Selenium wrapper
- v1.0.0: Initial release

## Notes

This package has not been released to PyPi so pip installing doesn't work!
