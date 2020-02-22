import socket
import os
import shutil

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

	def verify_ledger(self):
		pass


if __name__ == "__main__":
	client = Client()
