#!/usr/bin/env python

import os
from setuptools import setup, find_packages
__version__ = "0.1.2"


scripts = ["bin/" + j for j in os.listdir("bin") ]

requires = [
    "numpy",
    "astropy",
    "multiprocessing",
    "cleanmask"
]


setup(name = "rm-synthesis",
    version = __version__,
    description = "Performs Rotation Measurement(RM) Synthesis and RM Cleaning on FITS Cube Images",
    author = "Lerato Sebokolodi",
    author_email = "mll.sebokolodi@gmail.com",
    url = "https://github.com/Sebokolodi/RMSYNTHESIS/",
    packages = find_packages(),
    install_requires = requires,
    scripts = scripts, 
    license = "GNU GPL v2",
    classifiers = [],
 )
