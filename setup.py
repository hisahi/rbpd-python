#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from distutils.core import setup
import sys

if sys.version_info < (3, 3):
    sys.exit('Only Python >= 3.3 is supported')

setup(name='rbpd-python',
      version='0.1',
      description='RBP (random bytestream protocol) daemon for Python 3',
      author='Sampo Hippelainen',
      author_email='sampo.hippelainen AT gmail.com',
      python_requires='>3.3',
      packages=['rbpd-python']
      )
