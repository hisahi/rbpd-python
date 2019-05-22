#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
rbpd-python - RBP daemon for Python 3

Copyright (C) 2019 Sampo Hippeläinen

RBPD (RBP daemon) is a simple implementation of a
server for RBP (random bytestream protocol), a simple
protocol intended for testing purposes.
"""

import ipaddress
import socket
from .constants import IPV4, IPV6


def validate_port(port):
    return 0 <= port <= 65535


def validate_ip_address(ip, ipver):
    if ip in ['0', 'localhost']:
        return True
    elif ipver == IPV4:
        try:
            ipaddress.IPv4Address(ip)
        except ValueError:
            return False
        else:
            return True
    elif ipver == IPV6:
        try:
            ipaddress.IPv6Address(ip)
        except ValueError:
            return False
        else:
            return True
    else:
        raise ValueError('invalid IP version given')


def convert_special_ip_address(ip, ipver):
    STAR_IPS = {IPV4: '0.0.0.0', IPV6: '::'}
    LOCALHOST_IPS = {IPV4: '127.0.0.1', IPV6: '::1'}

    if ipver not in [IPV4, IPV6]:
        raise ValueError('invalid IP version given')
    elif ip == '0':
        return STAR_IPS[ipver]
    elif ip == 'localhost':
        return LOCALHOST_IPS[ipver]
    elif not validate_ip_address(ip):
        raise ValueError('invalid IP address given')
    else:
        return ip


def get_socket_type_for_ipver(ipver):
    if ipver == IPV4:
        return socket.AF_INET
    elif ipver == IPV6:
        return socket.AF_INET6
    else:
        raise ValueError('invalid IP version given')


def format_ip_and_port(ipver, address, port):
    if ipver == IPV4:
        return '{}:{}'.format(address, port)
    elif ipver == IPV6:
        return '[{}]:{}'.format(address, port)
    else:
        raise ValueError('invalid IP version given')
