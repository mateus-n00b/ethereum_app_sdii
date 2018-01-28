# Client main functions
#
#
#
class client_functions():
    def __init__(self,client):
        self.client = client

    def show_available_methods(self):
        methods = self.client.system.listMethods()
        for m in methods:
            print m

    # Shares a file
    def upload_file(self,fp):
        try:
            upload = open(fp,'rb')
            self.client.upload_file(fp,upload.read())
            upload.close()
            return 1
        except:
            return 0

    # Download a file from server
    def download_file(self,fp):
        save_file = open(fp,'wb')
        try:
            save_file.write(self.client.download_file(fp))
            save_file.close()
            return 1
        except:
            return 0

    def hello_server(self):
        return self.client.hello_server(key)    
