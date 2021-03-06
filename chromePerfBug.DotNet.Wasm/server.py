import sys
import os

web_dir = os.path.join(os.path.dirname(__file__), 'out')
os.chdir(web_dir)

if sys.version_info[0] == 2:

    import SimpleHTTPServer
    import SocketServer

    PORT = 8001

    class Handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
        pass

    Handler.extensions_map['.wasm'] = 'application/wasm'

    httpd = SocketServer.TCPServer(("", PORT), Handler)

    print ("python 2 serving at http://localhost:{}".format(PORT))
    httpd.serve_forever()


if sys.version_info[0] == 3:
    
    import http.server
    import socketserver

    PORT = 8000

    Handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("python 3 serving at http://localhost:{}".format(PORT))
        httpd.serve_forever()

