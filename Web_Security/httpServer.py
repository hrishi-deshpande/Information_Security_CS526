#Obtained from standard python documentation.
import SimpleHTTPServer
import SocketServer

PORT = 31337

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)
print "Serving at port", PORT

httpd.serve_forever();
