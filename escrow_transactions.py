import requests
import json
url_accounts_hist = 'https://data.ripple.com/v2/accounts/%s/transactions?result=tesSUCCESS&limit=1000' # i know, bad to set limit to 1000. Implement via marker
all_account_txs = {}
accounts=['rDdXiA3M4mYTQ4cFpWkVXfc2UaAXCFWeCK','rKDvgGUsNPZxsgmoemfrgXPS2Not4co2op','rf1BiGeXwwQoi8Z2ueFYTEXSwuJYfV2Jpn']
ESCROW_CREATE_TYPE ='EscrowCreate'
TRANSACTION_TYPES = [ESCROW_CREATE_TYPE]
#TODO change to a class and handle all account types with marker. Once done will have a separate caller class with pandas dataframe to get only the escrow create txns and the 
#common account roots with Escrow Finish , Re escrow, Sold etc
def get_json(url):
	with requests.get(url) as response:
		json_data = json.loads(response.text)
		#print (json_data)
		return json_data

def get_all_transactions(account):
	print('Getting Account Transaction History'  + account)
	url_account_hist =  url_accounts_hist%account
	return get_json(url_account_hist)
	

def get_account_transactions_history(account,**kargs):
	#print ('Getting Json for account')
	get_transactions = {'Payment':None,ESCROW_CREATE_TYPE:None,'EscrowCancel':None} #add more
	transaction_type = kargs.get(type)
	if transaction_type is None:
		return get_all_transactions(account)
	elif transaction_type in TRANSACTION_TYPES:
		return get_all_transactions[transaction_type](account)
		
if __name__ == "__main__":
	for account in accounts:
		all_account_txs[account] = get_account_transactions_history(account)
	print all_account_txs