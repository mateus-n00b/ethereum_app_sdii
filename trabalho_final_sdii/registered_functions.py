from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from ethereum.tools import tester as T

DEFAULT_PORT = 8000 # NOTE: if alterate this arg so you should update all whole code




class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

server = SimpleXMLRPCServer(("localhost",DEFAULT_PORT),requestHandler=RequestHandler)
server.register_introspection_functions()
TRANSACTIONS = dict() # To Check the current TRANSACTIONS

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
    def validate_transaction(self,key):
        return 1

    def download_file(self,fp):
        try:
            down_file = open(fp,"rb")
            return down_file.read()
        except:
            return 0

server.register_instance(Services())

def run():
    global server
    server.serve_forever()
