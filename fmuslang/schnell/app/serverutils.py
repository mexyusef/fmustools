import http.server
import os
import socket
import socketserver
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pyngrok import conf, ngrok



http_server_info = {}
ngrok_info = {}
conf.get_default().auth_token = "2DRXKuoTfxelo3N49y3NS4PwwTp_3L9i9MJcXXmdrwwKTq9bu"

class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # data = str(self.request.recv(1024), 'ascii')
        data = self.request.recv(1024).decode('utf8')
        cur_thread = threading.current_thread()
        response = bytes("{}: {}".format(cur_thread.name, data), 'ascii')
        self.request.sendall(response)


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


# https://stackoverflow.com/questions/14088294/multithreaded-web-server-in-python
class ThreadingSimpleServer(socketserver.ThreadingMixIn, HTTPServer):
    pass



def kunci(HOST, PORT):
    return f"{HOST}:{PORT}"


# PORT = 8000
# Handler = http.server.SimpleHTTPRequestHandler
# with socketserver.TCPServer(("", PORT), Handler) as httpd:
#     print("serving at port", PORT)
#     httpd.serve_forever()
# https://docs.python.org/3.5/library/socketserver.html#asynchronous-mixins
def run_quick(HOST="localhost", PORT=8080):
    if kunci(HOST, PORT) in http_server_info:
        stop_quick(HOST, PORT)
    server = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)
    http_server_info[kunci(HOST, PORT)] = {'server': server, 'thread': None}
    server.serve_forever()


def stop_quick(HOST="localhost", PORT=8080):
    print(f"Stop server {HOST}:{PORT}")
    if kunci(HOST, PORT) in http_server_info:
        server = http_server_info[kunci(HOST, PORT)]['server']
        print(f"Shutting down server {kunci(HOST, PORT)}...")
        server.shutdown()
        print(f"Closing server {kunci(HOST, PORT)}...")
        server.server_close()
        return True
    else:
        print(f"""[stop_quick]
        {kunci(HOST, PORT)} not found in {http_server_info}
        """)
        return False


def client(ip, port, message):
    """
    client(ip, port, "Hello World 1")
    client(ip, port, "Hello World 2")
    client(ip, port, "Hello World 3")
    """
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((ip, port))
        sock.sendall(bytes(message, 'ascii'))
        response = str(sock.recv(1024), 'ascii')
        print("Received: {}".format(response))


def run_server(HOST="localhost", PORT=0):
    print(f"Start server {HOST}:{PORT}")
    # Port 0 means to select an arbitrary unused port
    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    ip, port = server.server_address
    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    server_thread = threading.Thread(target=server.serve_forever)
    # Exit the server thread when the main thread terminates
    server_thread.daemon = True
    server_thread.start()
    print("Server loop running in thread:", server_thread.name)

    # client(ip, port, "Hello World 1")
    # client(ip, port, "Hello World 2")
    # client(ip, port, "Hello World 3")
    http_server_info[kunci(HOST, PORT)] = {'server':server, 'thread':server_thread}
    return (HOST, PORT)
    # server.shutdown()
    # server.server_close()


def close_server(HOST, PORT):
    print(f"Stop server {HOST}:{PORT}")
    if kunci(HOST, PORT) in http_server_info:
        server = http_server_info[kunci(HOST, PORT)]['server']
        server_thread = http_server_info[kunci(HOST, PORT)]['thread']
        print(f"Stopping {server_thread.name}...")
        # server_thread.stop()/terminate()/close()
        server.shutdown()
        server.server_close()
        server_thread.join()
        return True
    else:
        print(f"""[close_server]
        {kunci(HOST, PORT)} not found in {http_server_info}
        """)
        return False


def start_thread_server1(HOST="localhost", PORT=8080, USE_HTTPS=False):
    server = ThreadingSimpleServer((HOST, PORT), SimpleHTTPRequestHandler)
    if USE_HTTPS:
        import ssl
        # openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
        server.socket = ssl.wrap_socket(server.socket, keyfile='./key.pem', certfile='./cert.pem', server_side=True)
    
    http_server_info[kunci(HOST, PORT)] = {'server':server, 'thread':None}
    server.serve_forever()
    # return (HOST, PORT)


def stop_thread_server1(HOST="localhost", PORT=8080):
    print(f"Stop server {HOST}:{PORT}")
    if kunci(HOST, PORT) in http_server_info:
        server = http_server_info[kunci(HOST, PORT)]['server']
        # server_thread = http_server_info[kunci(HOST, PORT)]['thread']
        # print(f"Stopping {server_thread.name}...")
        # server_thread.stop()/terminate()/close()
        server.shutdown()
        server.server_close()
        # server_thread.join()
        return True
    else:
        print(f"""[stop_thread_server1]
        {kunci(HOST, PORT)} not found in {http_server_info}
        """)
        return False


def ngonek(port=80, proto='tcp'):
    tunnel = ngrok.connect(port, proto)
    ngrok_info[port] = tunnel
    return tunnel


def diskonek(tunnel):
    ngrok.disconnect(tunnel.public_url)


def nutup(port=80, forced=False):
    if forced:
        tunnel = ngrok_info[port]
        ngrok.disconnect(tunnel.public_url)
    elif port in ngrok_info:
        tunnel = ngrok_info[port]
        ngrok.disconnect(tunnel.public_url)
    else:
        print(f'port {port} not found in {ngrok_info}')


def aktif():
    return ngrok.get_tunnels()


def monitor(callback):
    """
    def callback(log): 
        print(str(log))
    """
    conf.get_default().log_event_callback = callback


def serve_directory_in_thread(directory_path, port=8000):
    """
    directory_path = "/path/to/your/directory"  # Replace this with the actual directory path you want to serve
    serve_directory_in_thread(directory_path)
    """
    class NonBlockingHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
        def end_headers(self):
            self.send_header('Access-Control-Allow-Origin', '*')
            super().end_headers()

    os.chdir(directory_path)

    handler = NonBlockingHTTPRequestHandler
    httpd = socketserver.TCPServer(("", port), handler)

    print(f"Serving directory at http://localhost:{port}/")

    # Create a new thread to run the server
    server_thread = threading.Thread(target=httpd.serve_forever)

    # Set the thread as a daemon, so it will be terminated when the main program exits
    server_thread.daemon = True

    # Start the server thread
    server_thread.start()

    try:
        # Keep the main thread running by doing some work
        while True:
            pass
    except KeyboardInterrupt:
        # If the user interrupts the main program (e.g., using Ctrl+C),
        # gracefully shut down the server and terminate the thread.
        print("\nShutting down server...")
        httpd.shutdown()


def serve_directory_in_thread_returning(directory_path, port=8000):
    """
    directory_path = "/path/to/your/directory"  # Replace this with the actual directory path you want to serve
    server = serve_directory_in_thread(directory_path)

    try:
        # Keep the main thread running until the user decides to stop the server
        while True:
            pass
    except KeyboardInterrupt:
        # If the user interrupts the main program (e.g., using Ctrl+C),
        # gracefully shut down the server and terminate the thread.
        print("\nShutting down server...")
        server.shutdown()

    """
    class NonBlockingHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
        def end_headers(self):
            self.send_header('Access-Control-Allow-Origin', '*')
            super().end_headers()

    os.chdir(directory_path)

    handler = NonBlockingHTTPRequestHandler
    httpd = socketserver.TCPServer(("", port), handler)

    print(f"Serving directory at http://localhost:{port}/")
    
    # Create a new thread to run the server
    server_thread = threading.Thread(target=httpd.serve_forever)

    # Set the thread as a daemon, so it will be terminated when the main program exits
    server_thread.daemon = True

    # Start the server thread
    server_thread.start()

    return httpd
