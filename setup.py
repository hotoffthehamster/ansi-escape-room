#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    # Note that distutils to be removed in Python 3.12.
    # - setuptools is not core Python. But it's assumed you have it
    #   if you ran pip to install this project, or if you installed
    #   a project that requires this project. So don't worry, it's
    #   very unlikely that distutils (this branch) being accessed.
    from distutils.core import setup

from ansi_escape_room import __version__


setup(
    name="ansi-escape-room",
    packages=["ansi_escape_room"],
    version=__version__,
    description="Simple library for color and formatting to terminal",
    long_description=open("README.rst").read(),
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
        "Operating System :: Microsoft",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Operating System :: POSIX :: Other",
        "Operating System :: OS Independent",
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
        "Topic :: Terminals"]
)
