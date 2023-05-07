from http.server import HTTPServer, BaseHTTPRequestHandler

class echoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Mengirim response code 200 OK
        self.send_response(200)
        
        # Mengatur header response
        self.send_header('content-type', 'text/html')
        self.end_headers()
        
        # Mengirim response message
        message = '404 Not Found'
        self.wfile.write(message.encode())  # Menggunakan method 'write' dari 'wfile' object

def main():
    PORT = 8080
    server = HTTPServer(('localhost', PORT), echoHandler)  # Menggunakan alamat IP localhost untuk test
    print('Server running on port %s' % PORT)
    server.serve_forever()

if __name__ == '__main__':
    main()
