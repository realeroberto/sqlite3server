# sqlite3server - A SQLite client/server wrapper.
#
# The MIT License (MIT)
# 
# Copyright (c) 2017-8 Roberto Reale
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import pickle
import socketserver
import sqlite3

class RequestHandler(socketserver.BaseRequestHandler):

    def _execute(self, stmt):
        self.cursor.execute(stmt)
        return self.cursor.fetchall()

    def setup(self):
        self.cursor = self.server.cursor

    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()

        # execute the query
        dataset = self._execute(self.data.decode('utf-8'))
        self.request.sendall(pickle.dumps(dataset))

        print("{} wrote:".format(self.client_address[0]))


class Server(socketserver.TCPServer):
    def __init__(self, server_address):

        # Connect to the database
        self.conn = sqlite3.connect('example.db')
        self.cursor = self.conn.cursor()

        # Call parent constructor
        super(Server, self).__init__(server_address, RequestHandler)

    def __del__(self):
        self.conn.close()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
