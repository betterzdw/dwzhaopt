#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="dwzhaopt",
    version="0.0.3",
    author="dwzhao",
    author_email="flybx@foxmail.com",
    description="An demonstration of how to create, test, document and publish to pypi.org.",
    license='MIT License',
    keywords="pip test document tutorial",
    url="https://github.com/betterzdw/dwzhaopt",
    packages=find_packages(),
    long_description=long_description,
    python_requires=">=2.7.9",

    entry_points={
        'console_scripts': [
            'dwzhao-echo = dwzhaopt.script:echo',
        ],
    },
)
