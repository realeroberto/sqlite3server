# sqlite3server

[![PyPI](https://img.shields.io/pypi/v/sqlite3server.svg)](https://pypi.python.org/pypi/sqlite3server)

A SQLite client/server Python 3 wrapper.

### Usage

        $ pip3 install sqlite3server

        $ sqlite3 example.db < examples/example.sql

        $ sqlite3server &

        $ python3 examples/client.py 'SELECT * FROM EXAMPLE'
        [(0,), (1,), (2,)]

### TODO

Implement a proper multithreading model (see for example https://stackoverflow.com/questions/393554/python-sqlite3-and-concurrency) and from there add tests.
