import socket
import os
import shutil
import uuid
import re

class Server:

	def __init__(self):
		global conn, addr
		self.sfile = None

		self.send_smac()

		'''
		s = socket.socket()
		host = socket.gethostname()
		print(f"host: {host}")
		port = 908
		s.bind((host,port))
		s.listen(1) #only one connection

		conn, addr = s.accept()
		print('[+] Client has connected')

		self.sfile = self.get_file()
		self.send_file()
		'''

	def get_file(self):
		file = input(str("[+] Input the name of the file you would like to send: ")) #holds path to files
		return file

	def send_file(self):
		cwd = os.getcwd()
		f = open(f"{cwd}/uploads/{self.sfile}", 'rb')
		file_data = f.read(1024)
		conn.send(file_data) #file sent in utf-8 bytes

	def send_smac(self):
		#function to send mac address to miner
		s = socket.socket()
		host = socket.gethostname()
		print(f"host: {host}")
		port = 909
		s.bind((host, port))
		s.listen(1)

		smac = self.get_smac()

		conn, addr = s.accept()
		conn.send(bytes(smac, "utf-8"))

	def get_smac(self):
		mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
		return mac

	def verify_ledger(self):
		pass

if __name__ == "__main__":
	server = Server()
