#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    
    name = 'pywifi2',

    version = '1.1',

    author = 'Phil H',

    description = "A module for manipulating WiFi devices.",

    long_description_content_type = "text/markdown",

    packages = find_packages(),

    install_requires = 'comtypes',

    python_requires = ">=3.13",

    url = 'https://github.com/minefarts/pywifi2', 

    download_url = 'https://github.com/minefarts/pywifi2/archive/master.zip',

    keywords = ['wifi', 'wireless', 'Windows']

)
