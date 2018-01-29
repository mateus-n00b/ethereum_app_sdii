#!/usr/bin/env python2.7
import xmlrpclib
import discovery_protocol as dp
import client_functions
from ethereum.tools import tester as T

DEFAULT_PORT = 8000 # Server default port
servers = dp.discovery() # Try to find providers in the network

def show_servers_fees():
    cont = 0 # index
    option = dict()

    for key in servers.keys():
        option[cont] = key
        print "{0} - Server: {1}".format(cont,key),
        print str(servers[key])
        cont+=1

    index = int()
    while 1:
        index = int(raw_input("Choose a server (number): "))
        if not option.has_key(index): # Invalid option?
            print "Invalid option! (Press Ctrl+C to exit, if you wish.)"
            continue
        break

    return option[index]

def main():
    server_addr = show_servers_fees() # Client choose an server
    server_addr = 'localhost' # TODO: < - ##### Delete this line #####

    try:
        # Establishing a connection
        client = xmlrpclib.ServerProxy("http://{0}:{1}".format(server_addr,DEFAULT_PORT))
    except:
        print "Error on conect to server! Exiting"
        exit(-1)

    functions = client_functions.client_functions(client)
    # Perform RPC
    functions.show_available_methods()

if __name__ == '__main__':
    main()
