#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
rbpd-python - RBP daemon for Python 3

Copyright (C) 2019 Sampo Hippeläinen

RBPD (RBP daemon) is a simple implementation of a
server for RBP (random bytestream protocol), a simple
protocol intended for testing purposes.
"""

import socket
from threading import Thread
from .constants import BUFFER_SIZE
from .algo import random_bytes
from .utils import get_socket_type_for_ipver


class RBPDServerTCP():
    def __init__(self, ipver, bind, port):
        self.ipver = ipver
        self.bind = bind
        self.port = port

    def get_socket(self):
        sock = socket.socket(get_socket_type_for_ipver(self.ipver),
                             socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((self.bind, self.port))
        return sock

    def handle_client(self, conn, address):
        with conn:
            while True:
                data = conn.recv(BUFFER_SIZE)
                if not data:
                    break
                conn.sendall(random_bytes(len(data)))

    def run(self):
        sock = self.get_socket()
        try:
            sock.listen()
            while True:
                conn, address = sock.accept()
                Thread(target=self.handle_client,
                       args=(conn, address), daemon=True).start()
        finally:
            sock.close()


class RBPDServerUDP():
    def __init__(self, ipver, bind, port):
        self.ipver = ipver
        self.bind = bind
        self.port = port

    def get_socket(self):
        sock = socket.socket(get_socket_type_for_ipver(self.ipver),
                             socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((self.bind, self.port))
        return sock

    def run(self):
        sock = self.get_socket()
        try:
            while True:
                data, addr = sock.recvfrom(BUFFER_SIZE)
                sock.sendto(random_bytes(len(data)), addr)
        finally:
            sock.close()


class RBPDServer():
    def __init__(self, ipver, bind, port):
        self.ipver = ipver
        self.bind = bind
        self.port = port
        self.tcp = RBPDServerTCP(ipver, bind, port)
        self.udp = RBPDServerUDP(ipver, bind, port)

    def run(self):
        Thread(target=self.udp.run, daemon=True).start()
        self.tcp.run()
