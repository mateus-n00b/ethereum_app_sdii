# Creating discovery service protocol
# TODO: how to kill a thread in python???
# This module is used by the server side
from socket import *
import os,time
from threading import Thread

SLEEP_TIME = 1 # beacon interval
BROAD_PORT = 2222 # broadcast port


# dp = discovery protocol
dp = socket(AF_INET,SOCK_DGRAM)
dp.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
dp.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

# Beacon function
def beacon(sock):
    while 1:
        time.sleep(SLEEP_TIME)
        sock.sendto("hello",("<broadcast>",BROAD_PORT))

def run():
    # Starting thread
    thread = Thread(group=None,target=beacon,args=(dp,))
    thread.start()
