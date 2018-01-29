from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from ethereum.tools import tester as T
import os

# GLOBALS
DEFAULT_PORT = 8000 # NOTE: if alterate this arg so you should update all whole code
TRANSACTIONS = dict() # To Check the current TRANSACTIONS
FEES = dict() # Record
FEES_FILE = "fees.txt"

# RPC
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Setting up server
server = SimpleXMLRPCServer(("localhost",DEFAULT_PORT),requestHandler=RequestHandler)
server.register_introspection_functions()

# Register functions
# def adder_func(a,b):
#     return a+b
# server.register_function(adder_func,'add')
# TODO:
#      Funcao para publicar arquivo
#      Funcao para baixar arquivo
#      Funcao para listar arquivos
#      Funcao para criar Smart-Contracts
#      Smart-Contract para lidar com essas coisas

class Services():
    global TRANSACTIONS
    global FEES

    def upload_file(self, fp,text):
        try:
            save_file = open(fp,'wb')
            save_file.write(text)
            save_file.close()
            return 1
        except:
            return 0

    def hello_server(self):
        return

    # Check if consumer have sufficient funds
    def __validate_transaction(self,key):
        return 1

    def download_file(self,fp):
        try:
            down_file = open(fp,"rb")
            return down_file.read()
        except:
            return 0

server.register_instance(Services())

# Define the fees for each provided service from a fee file 
def set_fees(fees_file):
    try:
        fp = open(fees_file,"rb")
    except:
        print "Error on read fees file!"
        os.system("killall python2.7")

    for rows in fp.readlines():
        if rows[0] != "#": # Is a comment?
            FEES[rows.split(':')[0]] = rows.split(':')[1].rstrip() # Read the fees file and update the FEES

def run():
    global server
    set_fees(FEES_FILE)
    # Have fees on file?
    if len(FEES):
        server.serve_forever()
    else:
        print "Check your fees file!"
        os.system("killall python2.7")
