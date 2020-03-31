#!/usr/bin/env python3
import os
import http.server
import socketserver
from datetime import datetime, timezone

## quick 'n dirty hello world to test container backend/proxy services

PORT = int(os.environ.get('PORT', '80'))

if __name__ == "__main__":
    Handler = http.server.SimpleHTTPRequestHandler

    with open('index.html', 'w') as file:
        file.write(u"""
           <h1 style="text-align: center">My py/container Hello World!!!</h1>
           <h2 style="text-align: center">Local IP %s - port %s </h2>
           """ % (
             socket.gethostbyname(socket.gethostname()), PORT
         ))

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()