import http.server
import socketserver
import threading
import time

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/stop':
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Stopping the server')
            # Останавливаем сервер, вызвав метод сервера
            self.server.stop()
        else:
            super().do_GET()

class StoppableServer(socketserver.TCPServer):
    allow_reuse_address = True

    def run(self):
        try:
            # Сервер работает до получения сигнала для остановки
            self.serve_forever()
        except KeyboardInterrupt:
            pass
        finally:
            self.server_close()

    def stop(self):
        # Закрываем сервер
        self.shutdown()

def start_server():
    PORT = 3000

    Handler = MyHandler

    httpd = StoppableServer(("", PORT), Handler)
    print(f"Serving at port {PORT}")

    # Запускаем сервер в отдельном потоке
    server_thread = threading.Thread(target=httpd.run)
    server_thread.start()
    return httpd

def stop_server(httpd):
    # Останавливаем сервер
    httpd.stop()

if __name__ == "__main__":
    # Запускаем сервер
    httpd = start_server()

    # Останавливаем сервер через 5 секунд
    time.sleep(5)
    stop_server(httpd)
