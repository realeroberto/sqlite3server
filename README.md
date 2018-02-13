# sqlite3server

[![PyPI](https://img.shields.io/pypi/v/sqlite3server.svg)](https://pypi.python.org/pypi/sqlite3server)

A SQLite client/server Python 3 wrapper.

### Usage

        $ sqlite3 example.db
        sqlite> create table test(number id);
        sqlite> insert into test values (0);
        sqlite> insert into test values (1);
        sqlite> insert into test values (2);

        $ python3 sqlite3server/sqlite3server.py &
        $ python3 examples/client.py 'SELECT * FROM TEST'
        [(0,), (1,), (2,)]

