import json
import os
import time  # Import the time module for the delay
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # Serve the index.html file
        if self.path == "/":
            try:
                # Read the index.html file
                with open("index.html", "r") as file:
                    html_content = file.read()

                # Send the response
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(html_content.encode())
            except FileNotFoundError:
                self.send_error(404, "File Not Found")
        if self.path == "/done?":
            print("Done!")
            self.send_response(200)
        else :
            print(self.path)
        
    def do_POST(self):
        # Handle the POST request for the form submission
        if self.path == "/":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)

            try:
                data = json.loads(post_data)
                ssid = data.get('ssid')
                password = data.get('password')

                # Simulate connection logic here (replace this with your actual code)
                if ssid and password:
                    # Simulate delay for the loading screen
                    time.sleep(1)  # Add a 3-second delay before sending the response
                    response = {
                        'status': 'success',
                        'title': f'Connected ',
                        'message': 'You can now disconnect from the ESP32 network and reconnect to your own Wi-Fi. The board will remain connected to your Wi-Fi.',
                        'ssid': ssid
                    }
                else:
                    response = {
                        'status': 'error',
                        'message': 'Missing SSID or password'
                    }
            except json.JSONDecodeError:
                response = {
                    'status': 'error',
                    'message': 'Invalid JSON format'
                }

            # Send the response in JSON format
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(response).encode())

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
