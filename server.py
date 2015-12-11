import SimpleHTTPServer
import SocketServer
import process
import subprocess
import sys
import urlparse

class myHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse.urlparse(self.path)
        amount = urlparse.parse_qs(parsed_path.query)['amt'][0]
        s_name = urlparse.parse_qs(parsed_path.query)['sname'][0]
        r_name = urlparse.parse_qs(parsed_path.query)['rname'][0]
        print "Sending ", str(amount), " from ", s_name, " to ", r_name
        #amount = 100
        sys.argv = ['processmain.py', str(amount), s_name, r_name]
        execfile("processmain.py")
        print self.path
        #call(["python", "process.py", amount])
PORT = 8000
handler = SocketServer.TCPServer(("", PORT), myHandler)
print "serving at port 8000"
handler.serve_forever()

