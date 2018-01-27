#!/usr/bin/env python2.7
import xmlrpclib
import discovery_protocol as dp
from ethereum.tools import tester as T

server_addr = dp.discovery()
DEFAULT_PORT = 8000

# TODO: Remove this, because my router are blocking requests to port 8000
server_addr = 'localhost' # Delete this line
client = xmlrpclib.ServerProxy("http://{0}:{1}".format(server_addr,DEFAULT_PORT))

def show_available_methods():
    methods = client.system.listMethods()
    for m in methods:
        print m

# Shares a file
def upload_file(fp):
    try:
        upload = open(fp,'rb')
        client.upload_file(fp,upload.read())
        upload.close()
        return 1
    except:
        return 0

# Download a file from server
def download_file(fp):
    save_file = open(fp,'wb')
    try:
        save_file.write(client.download_file(fp))
        save_file.close()
        return 1
    except:
        return 0

def hello_server():
    return client.hello_server(key)


show_available_methods()
download_file("foo")
