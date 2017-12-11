#from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from http.server import BaseHTTPRequestHandler, HTTPServer
from os import curdir, sep
from copyFiles import copyFiles
from imageConverter import imageConverter



PORT_NUMBER = 8080


class serverHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET(self):
    
		if self.path=="/lsss/rest/echosounder/love1?width=400":
	    
			self.path="/images/width=400"
       
		try:    
			sendReply = False
			if self.path.endswith(".html"):
				mimetype='text/html'
				sendReply = True
			if self.path.endswith("width=400"):
				mimetype='image/jpg'
				sendReply = True
      
			if sendReply == True:
				#Open the static file requested and send it
				f = open(curdir + sep + self.path , 'rb') 
				self.send_response(200)
				self.send_header('Content-type',mimetype)
				self.end_headers()
				self.wfile.write(f.read())
                #self.wfile.write(response)
				f.close()
			return

		except IOError:
			self.send_error(404,'File Not Found: %s' % self.path)


if __name__ == '__main__':
	try:
		
		copyFiles()
		imageConverter()
		#Create a web server and define the handler to manage the
		#incoming request
		server = HTTPServer(('', PORT_NUMBER), serverHandler)
		print('Started httpserver on port ' , PORT_NUMBER)
		
		#Wait forever for incoming htto requests
		server.serve_forever()
		
	except KeyboardInterrupt:
		print('^C received, shutting down the web server')
		server.socket.close()