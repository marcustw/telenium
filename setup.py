from setuptools import find_packages, setup

setup(
    name="telenium",
    version="1.0",
    description="Clean browser automation based on Selenium",
    keywords="telenium selenium browser automation efficient",
    author="marcustw (Marcus)",
    author_email="marcustanwei1@gmail.com",
    url="https://github.com/marcustw/telenium",
    python_requires=">=3.10",
    packages=find_packages(),
    install_requires=["selenium==4.8.3"],
    package_data={"telenium.src": ["webdrivers/**/*"]},
    test_suite="tests",
)
