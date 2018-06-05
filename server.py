import socket
import os
import requests
# from lxml.html import fromstring
from HTMLParser import HTMLParser

def Main():
		# host = '127.0.0.1'
		# port = 5000

		# s = socket.socket()
		# s.bind((host, port))

		# s.listen(1)
		# c, addr = s.accept()
		# print 'Connection from: ' + str(addr)
		# while True:
		# data = c.recv(4096)
		data = 'http://www.purplemath.com/modules/index.htm'
		# if not data:
		# 		break
		r = requests.get(data)
		print type(r.content) is str 
		
		# create a subclass and override the handler methods
		class MyHTMLParser(HTMLParser):

		    def handle_starttag(self, tag, attrs):
		    	if tag == 'a':
		    			print "Encountered a start tag:", tag
		    			for attr in attrs:
		    				for att in attr:
		    					if att == 'href':
		    			        		print "     href:", attr[1]

		parser = MyHTMLParser()
		parser.feed(r.content)

if __name__ == '__main__':
		Main()


