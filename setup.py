from setuptools import setup, find_packages

setup(
    name='vapeum',
    version='1.0',
    description='Clean browser automation based on Selenium',
    keywords='vapeum selenium browser automation efficient',
    author='marcustw (Marcus)',
    author_email='marcustanwei1@gmail.com',
    url='https://github.com/marcustw/vapeum',
    python_requires='>=3.10',
    packages=find_packages(),
    install_requires=['selenium==4.8.3'],
    package_data={
        'vapeum.src': ['webdrivers/**/*']
    },
    test_suite='tests'
    )
