import socket
import os

class Server:

	def __init__(self):
		self.file = None
		global conn, addr

		s = socket.socket()
		host = socket.gethostname()
		print(f"host: {host}")
		port = 1942
		s.bind((host,port))
		s.listen(1) #only one connection

		conn, addr = s.accept()
		print('[+] A client has connected')
		print(conn)

		self.get_file()
		self.send_file()

	def get_file(self):
		self.file = input(str("[+] Input the full path of the file you would like to send: ")) #holds path to files

	def send_file(self):
		f = open(self.file, 'rb')
		file_data = f.read(1024)
		conn.send(file_data)

if __name__ == "__main__":
    server = Server()
