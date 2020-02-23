import time
import datetime

class Block:

	def __init__(self, time, server, client, miner, file_hash, block_num, block_hash, block_prev_hash):

		#instance variables for when block created
		self.time = time
		self.server = server
		self.client = client
		self.miner = miner
		self.file = file_hash
		self.blockNum = block_num
		self.hash = block_hash
		self.prevHash = block_prev_hash

	def commit_to_ledger(self):
		cluster = MongoClient("mongodb+srv://Abhi:<password>@bsftp-ledger-lrklw.mongodb.net/test?retryWrites=true&w=majority")
		db = cluster["bsftp-ledger"]
		collection = db["transactions"]
		collection.insert_one({"_id": })
