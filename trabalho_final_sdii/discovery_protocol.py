# Listen for 'hello' messages
from socket import *
from threading import Thread
import time,os

BROAD_PORT = 2222
STATUS = False # Check if the server was found
SEARCH_TIME = 5 # maximal time to find a server

sock = socket(AF_INET,SOCK_DGRAM)

def status_checker():
    global STATUS
    time.sleep(SEARCH_TIME)
    if not STATUS:
        print "Sorry, but we can't find a service provider in this area!"
        os.system("killall python2.7")


def discovery():
    global BROAD_PORT
    global STATUS
    global SEARCH_TIME

    sock.bind(('',BROAD_PORT))
    servers = dict() # Servers found
    thread = Thread(group=None,target=status_checker)
    thread.start()

    start_timer = time.time() # To stop the search

    print "Searching servers..."
    while time.time() - start_timer <= SEARCH_TIME:
        data, addr = sock.recvfrom(1024)
        if  "hello" in data and not servers.has_key(addr[0]):
            STATUS = True # One Server found!
            servers[addr[0]] = str(data).replace('hello','')
    return servers

# Testing
# print discovery()
