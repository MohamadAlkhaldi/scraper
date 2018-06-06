import socket
import os
import requests
from HTMLParser import HTMLParser
# import mysql.connector as mariadb

def Main():
		# mariadb_connection = mariadb.connect(user='python_user', password='some_pass', database='employees')
		# cursor = mariadb_connection.cursor()

		host = '127.0.0.1'
		port = 5000

		s = socket.socket()
		s.bind((host, port))

		s.listen(1)
		c, addr = s.accept()
		print 'Connection from: ' + str(addr)
		while True:
				data = c.recv(4096)
				url = 'http://www.purplemath.com/modules/'
				links = []
				r = requests.get(data)
				feed = r.content[32852:37575]
				class MyHTMLParser(HTMLParser):
  
				    def handle_starttag(self, tag, attrs):
				    	if tag == 'a':
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


