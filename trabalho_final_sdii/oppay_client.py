#!/usr/bin/env python2.7
import xmlrpclib
import discovery_protocol as dp
import client_functions
from ethereum.tools import tester as T

DEFAULT_PORT = 8000 # Server default port
server_addr = dp.discovery() # Try to find providers in the network

# TODO: Remove this, because my router are blocking requests to port 8000
server_addr = 'localhost' # Delete this line
client = xmlrpclib.ServerProxy("http://{0}:{1}".format(server_addr,DEFAULT_PORT))

def main():
    global client

    functions = client_functions.client_functions(client)
    functions.show_available_methods()
