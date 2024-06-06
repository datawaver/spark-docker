from setuptools import find_packages, setup

setup(
    name="tweets",
    version="0.2",
    author="felix.borchers",
    packages=find_packages(),
    install_requires=[
        "pymongo",
        "requests",
    ],
)
