from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading
import time


def start_server(port):
    server = HTTPServer(("localhost", port), SimpleHTTPRequestHandler)
    print(f"Server is running on port {port}")
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.start()
    return server, server_thread


if __name__ == "__main__":
    my_server, my_server_thread = start_server(3000)

    # Продолжайте выполнение других операций

    time.sleep(210)

    print("Server closed")
    my_server.shutdown()
    my_server_thread.join()
