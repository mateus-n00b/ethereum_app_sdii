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

    sock.bind(('',BROAD_PORT))
    thread = Thread(group=None,target=status_checker)
    thread.start()

    while 1:
        data, addr = sock.recvfrom(1024)
        if data == "hello":
            STATUS = True # Server found!
            return addr[0]

# Testing
# print discovery()
