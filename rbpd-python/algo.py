#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
rbpd-python - RBP daemon for Python 3

Copyright (C) 2019 Sampo Hippeläinen

RBPD (RBP daemon) is a simple implementation of a
server for RBP (random bytestream protocol), a simple
protocol intended for testing purposes.
"""

from os import urandom


def random_bytes(n):
    return urandom(n)
