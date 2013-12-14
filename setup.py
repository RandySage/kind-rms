#!/usr/bin/env python

from setuptools import setup, find_packages
from grind.settings import VERSION
DESCRIPTION = ("REST API for basic SQL interaction")

setup(
    name='GRIND',
    version=VERSION,
    description=DESCRIPTION,
    url='https://github.com/ransage/grind',
    packages=['grind'],
    install_requires=['setuptools','eve'],
    tests_require=['nose'],
    test_suite='src'
)
