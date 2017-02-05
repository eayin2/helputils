from distutils.core import setup
from setuptools import find_packages

setup(
    name="helputils",
    version="0.8.7",
    author="eayin2",
    author_email="eayin2@gmail.com",
    packages=find_packages(),
    url="https://github.com/eayin2/helputils",
    description="Bunch of random functions and classes that are useful.",
    install_requires=["gymail", "pymongo"],
)
