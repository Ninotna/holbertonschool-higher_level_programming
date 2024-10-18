#!/usr/bin/python3
"""
A simple HTTP server implementation using Python's built-in http.server library.
This server provides basic API functionality with endpoints for home, data, and status.
"""

import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """
    SimpleAPIHandler - Handles HTTP requests and serves responses for a basic API

    This handler supports the following GET requests:
    - '/'        : Returns a welcome message
    - '/data'    : Returns a JSON object containing user data
    - '/status'  : Returns a simple "OK" status message
    For any other paths, it returns a 404 Not Found error.
    """

    def do_GET(self):
        """
        do_GET - Handles GET requests for predefined endpoints

        Return:
        - 200 OK response with appropriate content for valid endpoints
        - 404 Not Found for unknown endpoints
        """
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')
        elif self.path == '/data':
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode('utf-8'))
        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'OK')
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Endpoint not found')


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler, port=8000):
    """
    run - Starts the HTTP server and listens for incoming requests

    @arg: server_class - The class used to create the server, defaults to HTTPServer
    @arg: handler_class - The request handler class, defaults to SimpleAPIHandler
    @arg: port - The port on which to run the server, defaults to 8000

    Return:
    None, but runs the HTTP server indefinitely
    """
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print("Serving on port {}...".format(port))
    httpd.serve_forever()


if __name__ == '__main__':
    run()
