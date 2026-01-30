#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    
    name = 'pywifi',

    version = '2.1',

    author = 'Phil H & Jiang Sheng-Jhih',

    author_email = '',

    description = "A cross-platform module for manipulating WiFi devices.",

    long_description = open('README.md', 'r').read(),

    long_description_content_type = "text/markdown",

    packages = find_packages(),

    install_requires = 'comtypes',

    python_requires = ">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",

    url = 'https://github.com/minefarts/pywifi', 

    license = 'MIT',

    download_url = 'https://github.com/minefarts/pywifi/archive/master.zip', 

    classifiers = [
        'Intended Audience :: Developers',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],

    keywords = ['wifi', 'wireless', 'Linux', 'Windows']

)
