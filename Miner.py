import os
import socket

class Miner:

	def __init__(self):
		self.smac = None #server mac address
		self.cmac = None #client mac address
		self.mmac = None #miner mac address

		self.get_server_mac()
		#pass

	def verify_ledger(self):
		pass

	def get_server_mac(self):
		s = socket.socket()
		port = 909
		host = self.query_hostname()

		print(f"[+] Connecting to {host} on port {port}")
		s.connect((host,port))

		encoded_smac = s.recv(1024)
		smac = encoded_smac.decode("utf-8")

		return smac

	def query_hostname(self):
		hostname = input(str("[+] Enter the hostname of the server:  "))
		return hostname

if __name__ == "__main__":
	miner = Miner()
