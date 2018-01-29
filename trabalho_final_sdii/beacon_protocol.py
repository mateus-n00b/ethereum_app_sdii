# Creating discovery service protocol
# TODO: how to kill a thread in python???
# This module is used by the server side
from socket import *
import os,time
from threading import Thread

SLEEP_TIME = 1 # beacon interval
BROAD_PORT = 2222 # broadcast port
FEES_FILE = "fees.txt"

# dp = discovery protocol
dp = socket(AF_INET,SOCK_DGRAM)
dp.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
dp.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

# Beacon function
def beacon(sock):
    global FEES_FILE
    try:
        fp = open(FEES_FILE,"r")
    except:
        print "Error on read fees file! Exiting..."
        exit(-1)

    hello_msg = "hello\n" # hello msg with fees

    for rows in fp.readlines():
        if str(rows)[0] != "#":
            hello_msg+="\t"+str(rows) # Getting fees
    # Sending beacons with server fees
    while 1:
        time.sleep(SLEEP_TIME)
        sock.sendto(hello_msg,("<broadcast>",BROAD_PORT))

def run():
    # Starting thread
    thread = Thread(group=None,target=beacon,args=(dp,))
    thread.start()
