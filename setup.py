#!/usr/bin/env python
# -*- coding: utf-8 -*-
from distutils.core import setup
from itertools import chain

pkg_name = 'paramnet'
license = 'MIT'
version = '0.1'

tests = ['paramnet.tests']
tests_require = ['pytest>=2.9.2']

extras_req = {
    'testing': ['pytest', 'pytest-cov', 'pytest-flakes', 'pytest-pep8', 'rstcheck']
}

extras_req['all'] = list(chain(extras_req.values()))

if __name__ == '__main__':
    setup(
        name=pkg_name.lower(),
        version=version,
        description="NetworkX graphs with required node/edge parameters",
        author="Sean P. Cornelius",
        author_email="spcornelius@gmail.com",
        license=license,
        packages=[pkg_name],
        install_requires=['networkx>=2.0', 'indexed.py', 'scipy'],
        tests_require=['pytest>=2.9.2', 'numpy'],
        extras_require=extras_req,
        python_requires='>=3.6')
