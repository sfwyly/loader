
from setuptools import setup, find_packages

setup(
    name="loader",
    version="1.0",
    keywords="request util",
    description="request",
    long_description="description",
    license="MIT Licence",

    author="sfwyly",
    packages=find_packages(),
    include_package_data=True,
    platforms="Windows",
    install_requires=['requests']

)
