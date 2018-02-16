#
# omnik-pvoutput-daemon is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# omnik-pvoutput-daemon is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
#

import logging
import socket  # Import socket module
import sys

import OmnikInverterMessage
from PvOutput import PvOutput


#
# The daemon which listens for all the connections.
#
class Daemon:
    def __init__(self):
        host = '0.0.0.0'                              #<<<< change this to your listing IP address >>>>>
        port = 9500
        self.server_sock = (host, port)

        # Datagram (tcp) socket
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)               # Create a socket object
            self.s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        except socket.error, msg:
            logging.warning('Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])

        # Bind socket to local host and port
        logging.info('Starting listing on %s port %s' % self.server_sock)
        try:
            self.s.bind(self.server_sock)
        except socket.error , msg:
            logging.warning('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
            sys.exit(1)
        finally:
            logging.info('Socket bind complete')

        try:
            self.s.listen(1)
        except socket.error, msg:
            logging.warning('Failed listen. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
            sys.exit(1)


    def run(self):
        pvoutput = PvOutput()

        while True:
            # receive data from client (data, addr)
            logging.info('Waiting for a connection on %s port %s' % self.server_sock)
            try:
                conn, client_addr = self.s.accept()
            except KeyboardInterrupt:
                logging.warning("You pressed Ctrl+C ... Aborting!\n")
                self.s.close()
                sys.exit()
            except socket.error, msg:
                logging.warning('Failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
                self.s.close()
                sys.exit(1)
            else:
                logging.info('Connection from: %s', client_addr)
            finally:
                data = conn.recv(1024)
                conn.close()
                logging.debug('Received data: %s', repr(data))

            if data:
                # This is where Woutrrr's magic happens ;)
                dmsg = OmnikInverterMessage.OmnikInverterMessage(data)
                pvoutput.process(dmsg)

            else:
                continue

        self.s.close()
