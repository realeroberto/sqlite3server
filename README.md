# sqlite3server

[![PyPI](https://img.shields.io/pypi/v/sqlite3server.svg)](https://pypi.python.org/pypi/sqlite3server)

A SQLite client/server Python wrapper.

### Usage

        $ sqlite3 example.db
        sqlite> create table test(number id);
        sqlite> insert into test values (0);
        sqlite> insert into test values (1);
        sqlite> insert into test values (2);

        $ python server.py &
        $ python client.py 'SELECT * FROM TEST'
        [(0,), (1,), (2,)]

