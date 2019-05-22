#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
rbpd-python - RBP daemon for Python 3

Copyright (C) 2019 Sampo Hippeläinen

RBPD (RBP daemon) is a simple implementation of a
server for RBP (random bytestream protocol), a simple
protocol intended for testing purposes.
"""

VERSION = '0.1'
DEFAULT_PORT = 5832
DEFAULT_BIND = 'localhost'

IPV4 = 4
IPV6 = 6

EXIT_SUCCESS = 0
EXIT_FAILURE = 1

BUFFER_SIZE = 2048
