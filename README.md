# vapeum

This is a package for using selenium browser automation tool that is much easier and requires less configuration. It should fit a typical use case of browser automation required. There is also auto clean up so you won't have to worry about the cleaning up.

```sh
pip install vapeum
```

Using vapeum

```python
from vapeum import vapeum

if __name__ == '__main__':
  with vapeum() as b:
    b.get('https://icanhazip.com')
    print(b.page_source)

```
