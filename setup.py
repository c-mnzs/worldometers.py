import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="worldometers.py",
    version="1.0.1",
    author="Carlos Menezes",
    author_email="talk@cmenezes.space",
    description="Get real time Earth statistics related to population.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/c-mnzs/worldometers.py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'appdirs>=1.4.3',
        'beautifulsoup4>=4.6.3',
        'bs4>=0.0.1',
        'certifi>=2018.8.24',
        'chardet>=3.0.4',
        'cssselect>=1.0.3',
        'fake-useragent>=0.1.10',
        'idna>=2.7',
        'lxml>=4.2.5',
        'parse>=1.8.4',
        'pyee>=5.0.0',
        'pyppeteer>=0.0.24',
        'pyquery>=1.4.0',
        'requests>=2.19.1',
        'requests-html>=0.9.0',
        'six>=1.11.0',
        'tqdm>=4.26.0',
        'urllib3>=1.23',
        'w3lib>=1.19.0',
        'websockets>=6.0'
    ]
)