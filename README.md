# vapeum

This is a package for using selenium browser automation tool that is much easier and requires less configuration. It should fit a typical use case of browser automation required. There is also auto clean up so you won't have to worry about the cleaning up.

```sh
pip install vapeum
```

Using vapeum

```python
from vapeum import Vapeum

if __name__ == "__main__":
    vapeum = Vapeum()
    with vapeum as b:
        b.get("https://www.google.com")
        print(f"{b.page_source[:100]}\n")
        for request in b.requests[:2]:
            if request.response:
                print(
                    f"url = {request.url}\nstatus_code = {request.response.status_code}, "
                    "response = {request.response.headers['Content-Type']}\n"
                )
        print()
    
    print("done")

```
