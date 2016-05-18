#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
setup.py is a part of colored.

Copyright 2014-2016 Dimitris Zlatanidis <d.zlatanidis@gmail.com>
All rights reserved.

Colored is very simple Python library for color and formatting in terminal.

https://github.com/dslackw/colored

colored is free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

from distutils.core import setup
from colored import __version__


setup(
    name="colored",
    packages=["colored"],
    version=__version__,
    description="Simple library for color and formatting to terminal",
    keywords=["color", "colour", "paint", "ansi", "terminal", "linux",
              "python"],
    author="dslackw",
    author_email="d.zlatanidis@gamil.com",
    url="https://github.com/dslackw/colored",
    package_data={"": ["LICENSE", "README.rst", "CHANGELOG"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
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
