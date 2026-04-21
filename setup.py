from setuptools import setup, find_packages

setup(
    name = 'pywifi2',
    version = '1.1',
    description = "A cross-platform module for manipulating WiFi devices.",
    packages = find_packages(),
    install_requires = ['philh_myftp_biz', 'pywifi'],
    python_requires = ">=3.14",
    url = 'https://github.com/minefarts/pywifi2', 
    license = 'MIT',
    download_url = 'https://github.com/minefarts/pywifi2/archive/master.zip'
)
