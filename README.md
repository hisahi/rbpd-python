# rbpd-python
A simple rbpd (RBP server) for Python 3. This is mostly a sample project.

# RBP
RBP (random bytestream protocol) is a simple protocol for both TCP and UDP. RBP does not send data on its own; for every byte the client sends, RBP servers must send - as a response - a random byte generated with an implementation-defined random number generation algorithm. For instance, if the client sends a 256 byte message, the server must respond with 256 random bytes.

# Install
Just run `python3 setup.py install`. After that you can use `python3 -m rbpd-python`. Note that the server by default only listens on localhost; see `--help` for available options.



