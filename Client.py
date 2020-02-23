import socket
import os
import re
import uuid
import hashlib

class Client:

	def __init__(self):
		self.cfile = None
		global s

		s = socket.socket()
		port = 908
		host = self.query_hostname()

		print(f"[+] Connecting to {host} on port {port}")
		s.connect((host,port))

		self.cfile = self.query_download()
		self.download_file()

	def query_hostname(self):
		hostname = input(str("[+] Enter the hostname of the server:  "))
		return hostname

	def query_download(self):
		file = input(str("[+] Input the name you would like the file to be saved to: ")) #holds path to files
		return file

	def download_file(self):
		cwd = os.getcwd()
		f = open(f"{cwd}/downloads/{self.cfile}", "w+")
		file_data = s.recv(1024) #get data from server peer
		decoded = file_data.decode("utf-8") #need to decode bytes that were sent by server
		f.write(decoded)
		f.close()

	def send_cmac(self):
		#function to send mac address to miner
		s = socket.socket()
		host = socket.gethostname()
		print(f"host: {host}")
		port = 909
		s.bind((host, port))
		s.listen(1)

		cmac = self.get_cmac()

		conn, addr = s.accept()
		conn.send(bytes(cmac, "utf-8"))

	def get_cmac(self):
		mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
		return mac

	def send_cfhash(self):
		s = socket.socket()
		host = socket.gethostname()
		print(f"host: {host}")
		port = 910
		s.bind((host, port))
		s.listen(1)

		cfhash = self.get_fhash()

		conn, addr = s.accept()
		conn.send(bytes(cfhash, "utf-8"))

	def get_fhash(self):
		cwd = os.getcwd()
		file = f"{cwd}/downloads/{self.cfile}"
		fhash = hashlib.sha256(open(file, 'rb').read()).hexdigest() #using sha256, stronger than md5
		return fhash

	def verify_ledger(self):
		pass


if __name__ == "__main__":
	client = Client()
