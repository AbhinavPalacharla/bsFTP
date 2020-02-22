import os
import socket
import re
import uuid

class Miner:

	def __init__(self):
		self.smac = None #server mac address
		self.cmac = None #client mac address
		self.mmac = None #miner mac address

		print(f"[+] Give the server hostname")
		self.smac = self.get_mac()

		print(f"[+] Give the client hostname")
		self.cmac = self.get_mac()

		self.mmac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))

	def verify_ledger(self):
		pass

	def get_mac(self):
		s = socket.socket()
		port = 909
		host = self.query_hostname()

		print(f"[+] Connecting to {host} on port {port}")
		s.connect((host,port))

		encoded_mac = s.recv(1024)
		mac = encoded_mac.decode("utf-8")

		return mac

	def query_hostname(self):
		hostname = input(str("[+] Enter the hostname:  "))
		return hostname

if __name__ == "__main__":
	miner = Miner()
