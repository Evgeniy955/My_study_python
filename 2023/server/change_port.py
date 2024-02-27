import os

REDIRECT_URI = "http://localhost:3000/"

def redirection_uri(self):
    new_uri = REDIRECT_URI
    return new_uri

def check_local_port():
    port = 3000
    data_port = os.popen(f"lsof -i :{port}").readlines()
    if len(data_port) != 0:
        while len(data_port) != 0:
            port += 1
            data_port = os.popen(f"lsof -i :{port}").readlines()
        uri = f"http://localhost:{port}/"
        print(uri)
    else:
        print(f"http://localhost:{port}/")


check_local_port()