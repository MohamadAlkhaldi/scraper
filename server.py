import socket
import os
import requests
# from lxml.html import fromstring
from HTMLParser import HTMLParser

def Main():
		host = '127.0.0.1'
		port = 5000

		s = socket.socket()
		s.bind((host, port))

		s.listen(1)
		c, addr = s.accept()
		print 'Connection from: ' + str(addr)
		while True:
				data = c.recv(4096)
				# data = 'http://www.purplemath.com/modules/index.htm'
				url = 'http://www.purplemath.com/modules/'
				links = []
				# if not data:
				# 		break
				r = requests.get(data)
				# # print r.content.find('<h3 class="section-title" align="center">Intermediate Algebra')
				# print r.content.find('<h3 class="section-title" align="center">Advanced Algebra Topics')
				feed = r.content[32852:37575]
				# print feed
				
				# create a subclass and override the handler methods
				class MyHTMLParser(HTMLParser):

				#     # def handle_starttag(self, tag, attrs):
				#     # 	print 'starting tag :' + tag
				#     def handle_data(self, data):
				#     	if data == 'Intermediate Algebra Topics':
				#     			print "Data     :", data
				#     	if data == 'Advanced Algebra Topics':
				#     			print "Data     :", data
				#     			HTMLParser.close()
				    
				    def handle_starttag(self, tag, attrs):
				    	if tag == 'a':
				    			# print "Encountered a start tag:", tag
				    			for attr in attrs:
				    				for att in attr:
				    					if att == 'href':
				    						links.append(url +attr[1])


				parser = MyHTMLParser()
				parser.feed(feed)
				print links
				res = ''
				for i in range(len(links)):
					res = res + links[i] + '\n'
				c.send(res)
		c.close()


if __name__ == '__main__':
		Main()


