from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl
import os

class CORSRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        SimpleHTTPRequestHandler.end_headers(self)

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

def run(server_class=HTTPServer, handler_class=CORSRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    
    # SSL configuration
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain(certfile='/Users/giorgos/Workspace/Projects/ssl-certs/cursor/cert.pem', keyfile='/Users/giorgos/Workspace/Projects/ssl-certs/cursor/key.pem')
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    
    print(f"Serving HTTPS on :: port {port} (https://[::]:{port}/)")
    httpd.serve_forever()

if __name__ == '__main__':
    run() 