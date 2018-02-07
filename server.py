import pickle
import SocketServer
import sqlite3

class MyTCPHandler(SocketServer.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # Connect to the database
        conn = sqlite3.connect('example.db')
        c = conn.cursor()

        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()

        # execute the query
        c.execute(self.data)
        dataset = c.fetchall()
        self.request.sendall(pickle.dumps(dataset))

        print "{} wrote:".format(self.client_address[0])

        conn.close()


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
