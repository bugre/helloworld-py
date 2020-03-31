#!/usr/bin/env python3
import os
import socket
import http.server
import socketserver
from datetime import datetime, timezone

## quick 'n dirty hello world to test container backend/proxy services

PORT = int(os.environ.get('PORT', '80'))

print ("To test, access: http://localhost and http://admin:admin@localhost:1936\n")

if __name__ == "__main__":
    Handler = http.server.SimpleHTTPRequestHandler

    with open('index.html', 'w') as file:
        file.write(u"""
           My py/container Hello World!!!<br>
           Local IP %s - port %s.
           """ % ( socket.gethostbyname(socket.gethostname()), PORT ))

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()