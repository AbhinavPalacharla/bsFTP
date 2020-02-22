import socket
import os
import shutil

class Client:

	def __init__(self):
		s = socket.socket()
		port = 1942
		host = self.query_hostname()

		print(f"[+] Connecting to {host} on port {port}")
		s.connect((host,port))

		cfile = self.query_download()

	def query_hostname(self):
		hostname = input(str("[+] Enter the hostname of the server:  "))
		return hostname

	def query_download(self):
		path = input(str("[+] Input the full path of the folder where you would like downloads to go: ")) #holds path to files
		return path

	def download_file(self):
		cwd = os.getcwd()
		shutil.rmtree(f"{cwd}/downloads")#clear downloads folder before usage
        f = open(cfile, "w+")
		file_data = f.recv(1024) #get data from server peer
		f.write(file_data) #write data to user dwfined file
		f.close()



client = Client()
