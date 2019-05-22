#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
rbpd-python - RBP daemon for Python 3

Copyright (C) 2019 Sampo Hippeläinen

RBPD (RBP daemon) is a simple implementation of a
server for RBP (random bytestream protocol), a simple
protocol intended for testing purposes.
"""

import argparse
import logging
import sys
from .constants import DEFAULT_BIND, DEFAULT_PORT, IPV4, IPV6, VERSION, \
                       EXIT_SUCCESS, EXIT_FAILURE
from .server import RBPDServer
from .utils import validate_ip_address, validate_port, \
                   convert_special_ip_address, format_ip_and_port


def get_parser():
    parser = argparse.ArgumentParser(
                        description=('rbpd-python {} - daemon server for RBP' +
                                     '(random bytestream protocol)')
                        .format(VERSION))
    parser.add_argument('-l', '--listen',
                        help='the IP to listen for (0 for any, ' +
                             'localhost only by default)',
                        default=DEFAULT_BIND)
    parser.add_argument('-p', '--port',
                        help='the port to listen for',
                        default=DEFAULT_PORT, type=int)
    return parser


def get_logger():
    logger = logging.getLogger('rbpd-python')
    stdout = logging.StreamHandler()
    stdout.setLevel(logging.INFO)
    logger.addHandler(stdout)
    return logger


def main(argv=sys.argv):
    parser = get_parser()
    args = parser.parse_args(argv[1:])

    ipver = IPV4
    bind = args.listen
    port = args.port

    if not validate_ip_address(bind, ipver):
        logger.error('invalid IP address given to bind')
        return EXIT_FAILURE
    if not validate_port(port):
        logger.error('invalid port given to port')
        return EXIT_FAILURE

    logger = get_logger()
    logger.setLevel(logging.INFO)

    bind = convert_special_ip_address(bind, ipver)
    server = RBPDServer(ipver=ipver, bind=bind, port=port)
    logger.info('Listening on port {} (TCP/UDP)'.format(
                                    format_ip_and_port(ipver, bind, port)))

    try:
        server.run()
    except KeyboardInterrupt:
        logger.info('Got ^C, exiting')

    return EXIT_SUCCESS

