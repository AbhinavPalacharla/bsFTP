import os
import socket
import re
import uuid
import datetime
#import Block
from Block import Block
#import pymongo
#from pymongo import MongoClient

class Miner:

	def __init__(self):
		self.smac = None #server mac address
		self.cmac = None #client mac address
		self.mmac = None #miner mac address
		self.server_fhash = None #file hash on server
		self.client_fhash = None #file hash on client
		self.fhash = None
		self.fintegrity = False

		print(f"[+] Give the server hostname")
		self.smac = self.get_smac()
		print(f"Server mac: {self.smac}")
		print(f"[+] Give the client hostname")
		self.cmac = self.get_cmac()
		print(f"Client mac: {self.cmac}")
		self.mmac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))

		self.server_fhash = self.get_sfhash()
		print(f"server file hash: {self.server_fhash}")

		self.client_fhash = self.get_cfhash()
		print(f"client file hash: {self.client_fhash}")

		self.generate_block()

		#print(self.client_fhash)

	def generate_block(self):
		time = datetime.datetime.now()
		self.verify_file_integrity()
		self.act_on_integrity()
		block = Block(time, self.smac, self.cmac, self.mmac, self.fhash)

	def act_on_integrity(self):
		if self.fintegrity == True:
			self.fhash = self.server_fhash
		else:
			self.fhash = "Invalid Transaction -- hashes did not match, file integrity not intact"

	def verify_file_integrity(self):
		if self.server_fhash == self.client_fhash:
			self.fintegrity = True
		else:
			self.fintegrity = False

	def get_smac(self):
		s = socket.socket()
		port = 909
		host = self.query_hostname()

		print(f"[+] Connecting to {host} on port {port}")
		s.connect((host,port))

		encoded_mac = s.recv(1024)
		mac = encoded_mac.decode("utf-8")

		return mac

	def get_cmac(self):
		s = socket.socket()
		port = 910
		host = self.query_hostname()

		print(f"[+] Connecting to {host} on port {port}")
		s.connect((host,port))

		encoded_mac = s.recv(1024)
		mac = encoded_mac.decode("utf-8")

		return mac

	def get_sfhash(self):
		s = socket.socket()
		port = 911
		host = self.query_hostname()

		print(f"[+] Connecting to {host} on port {port}")
		s.connect((host,port))

		encoded_fhash = s.recv(1024)
		fhash = encoded_fhash.decode("utf-8")

		return fhash

	def get_cfhash(self):
		s = socket.socket()
		port = 912
		host = self.query_hostname()

		print(f"[+] Connecting to {host} on port {port}")
		s.connect((host,port))

		encoded_fhash = s.recv(1024)
		fhash = encoded_fhash.decode("utf-8")

		return fhash


	def query_hostname(self):
		hostname = input(str("[+] Enter the hostname:  "))
		return hostname

if __name__ == "__main__":
	miner = Miner()
