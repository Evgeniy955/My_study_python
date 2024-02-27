from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading
import time


def start_server(port):
    server = HTTPServer(("localhost", port), SimpleHTTPRequestHandler)
    print(f"Server is running on port {port}")
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.start()
    return server, server_thread

def shutdown():
    print("Server closed")
    my_server.shutdown()
    my_server_thread.join()

if __name__ == "__main__":
    my_server, my_server_thread = start_server(3000)

    # Продолжайте выполнение других операций

    time.sleep(20)

    print("Server closed")
    my_server.shutdown()
    my_server_thread.join()




# def check_local_port():
#     """mac_os"""
#     info_port = None
#     port = os.popen("lsof -i :3000").readlines()
#     if len(port) != 0:
#         for text in port:
#             if "Python" in text:
#                 info_port = text.split(" ")
#         pid = [port_data for port_data in info_port if port_data.isdigit()]
#         command = f"kill {int(pid[0])}"
#         os.system(command)
#
# if __name__ == "__main__":
#     check_local_port()