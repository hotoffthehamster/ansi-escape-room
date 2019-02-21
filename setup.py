#!/usr/bin/python
# -*- coding: utf-8 -*-

import setuptools
from distutils.core import setup
from ansi_escape_room import __version__


setup(
    name="ansi-escape-room",
    packages=["ansi_escape_room"],
    version=__version__,
    description="Simple library for color and formatting to terminal",
    keywords=["color", "colour", "paint", "ansi", "terminal", "linux",
              "python"],
    author='HotOffThe Hamster',
    author_email='hotoffthehamster+ansiescaperoom@gmail.com',
    url="https://github.com/hotoffthehamster/ansi-escape-room",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        "Operating System :: POSIX :: Linux",
        "Operating System :: POSIX :: Other",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.0",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Unix Shell",
        "Topic :: Terminals"],
    long_description=open("README.rst").read()
)
