import time
import datetime
import pymongo
from pymongo import MongoClient
import hashlib
from hashlib import sha256
import random
from random import *
#cluster = MongoClient("mongodb+srv://Abhi:<password>@bsftp-ledger-lrklw.mongodb.net/test?retryWrites=true&w=majority")

class Block:

	#def __init__(self, time, server, client, miner, file_hash, block_num, block_hash, block_prev_hash):
	def __init__(self, time, server, client, miner, file_hash):
		#instance variables for when block created
		self.time = time
		self.server = server
		self.client = client
		self.miner = miner
		self.file = file_hash

		self.blockNum = None
		self.hash = None
		self.prevHash = None
		self.randomNum = 0

		self.commit_to_ledger()

	def generate_hash(self):

		#basic proof of work algorithm to generate hash of block

		seed(1) #seed random number generator
		randomNum = randint(1, 10000) #easy proof of work algorithm just for proof of concept, can be made mush more difficult by changing 10000 to 100000

		solution = 0
		a = 0
		b = 0

		while solution != randomNum:
			a = randint(1, 500)
			b = randint(1, 500)
			#print(f"a: {a}")
			#print(f"b: {b}")

			solution = a*b

		hashed_solution = hashlib.sha256(b'{solution}').hexdigest()

		return hashed_solution

	def get_prevHash(self):
		cluster = MongoClient("mongodb+srv://MinerA:BsftpMinerA@bsftp-ledger-lrklw.mongodb.net/test?retryWrites=true&w=majority")
		db = cluster["ledger"]
		collection = db["transactions"]

		a = 0
		for x in db.transactions.find({}, {"_id": "*"}):
			a += 1

		last_id = a - 1
		#last_id = db.transactions.count_documents({"time":"*"})

		document = db.transactions.find({"_id": last_id})
		print(document)
		#hash = document.get("block hash")

		#return hash

	def commit_to_ledger(self):
		cluster = MongoClient("mongodb+srv://MinerA:BsftpMinerA@bsftp-ledger-lrklw.mongodb.net/test?retryWrites=true&w=majority")
		db = cluster["ledger"]
		collection = db["transactions"]

		#self.block_num = db.transactions.count_documents({"time":"*"}) #get all blocks that have been commited at any time (hacky way to get # of blocks because .count() deprecated)

		a = 0

		for x in db.transactions.find({}, {"_id": "*"}):

			a += 1

		self.blockNum = a

		#print(self.blockNum)
		if self.blockNum == 0:
			self.genesis_block()

		self.hash = self.generate_hash()
		self.prevHash = self.get_prevHash()

		collection.insert_one({"_id": self.blockNum, "file hash": self.file, "server": self.server, "client": self.client, "miner": self.miner, "time of transaction": self.time, "block hash": self.hash, "previous hash": self.prevHash}) #insert block to ledger
		print('block inserted')

	def genesis_block(self):
		self.hash = self.generate_hash()

		cluster = MongoClient("mongodb+srv://MinerA:BsftpMinerA@bsftp-ledger-lrklw.mongodb.net/test?retryWrites=true&w=majority")
		db = cluster["ledger"]
		collection = db["transactions"]
		collection.insert_one({"_id":0, "file hash": self.file, "server": self.server, "client": self.client, "miner": self.miner, "time of transaction": self.time, "block_hash": self.hash}) #committing genesis block to ledger. Needed because there is no block with previous hash
		print('genesis block inserted')
