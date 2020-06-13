import requests
import cbpro
import json
import sys
from pprint import pprint


config = "" 

class Coinbase_Pro:
	def __init__(self, key, b64secret, passphrase):
		self.url = "https://api.pro.coinbase.com"
		self.auth_client = cbpro.AuthenticatedClient(key, b64secret, passphrase)
		self.public_client = cbpro.PublicClient()
		self.account_data_w_balance = []
		self.instrument_list = []
		self.set_account_data()

	#def request_trading_data():
		#self.auth_client.get_account("")

	def set_account_data(self):
		account_data_raw = self.auth_client.get_accounts()
		self.account_data_w_balance = []
		self.instrument_list = []
		for index in range(len(account_data_raw)):
			balance = float(account_data_raw[index]['balance'])
			if balance > 0.00:
				self.account_data_w_balance.append(account_data_raw[index])
				self.instrument_list.append(account_data_raw[index]['currency'])

	def return_message(self):
		return self.data

	def get_account_data(self):
		return self.account_data_w_balance

	def get_instrument_list(self):
		return self.instrument_list



def initialize_config(filename):
    with open(filename) as config_json:
        global config
        config = json.load(config_json)


def main():
	initialize_config(sys.argv[1])
	cb_client = Coinbase_Pro(config['coinbase_pro_key'], config['coinbase_pro_secret'], config['coinbase_pro_passphrase'])
	pprint(cb_client.get_account_data())
	pprint(cb_client.get_instrument_list())
main()
