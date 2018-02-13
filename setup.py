from setuptools import setup

setup(
    name = 'sqlite3server',
    version = '0.1.3',
    description = 'A SQLite client/server wrapper',
    packages = [ 'sqlite3server' ],
    author = 'Roberto Reale',
    author_email = 'rober.reale@gmail.com',
    url = 'https://github.com/robertoreale/sqlite3server',
    keywords = [ 'sqlite3', 'server', ],
    install_requires = [ ],
    test_suite = 'nose.collector',
    tests_require = ['nose'],
    entry_points={
        'console_scripts': [
            'sqlite3server = sqlite3server.__main__:main'
            ]
        },
)

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
