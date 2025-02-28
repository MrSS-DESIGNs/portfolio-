from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class SimpleServer(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data)

        name = data.get('name')
        email = data.get('email')
        message = data.get('message')

        print(f"Received: Name={name}, Email={email}, Message={message}")

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response = {"message": "Your info has been received!"}
        self.wfile.write(json.dumps(response).encode())

server = HTTPServer(('localhost', 8000), SimpleServer)
print("Server running on port 8000...")
server.serve_forever()
