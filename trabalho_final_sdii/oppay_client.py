#!/usr/bin/env python2.7
import xmlrpclib
import discovery_protocol as dp
import client_functions
from ethereum.tools import tester as T

DEFAULT_PORT = 8000 # Server default port
server_addr = dp.discovery() # Try to find providers in the network

print server_addr
# TODO: Remove this, because my router are blocking requests to port 8000
server_addr = 'localhost' # Delete this line
client = xmlrpclib.ServerProxy("http://{0}:{1}".format(server_addr,DEFAULT_PORT))

def main():
    global client

    # Creating object client
    functions = client_functions.client_functions(client)
    # Perform RPC
    functions.show_available_methods()

if __name__ == '__main__':
    main()
