#!/usr/bin/python

import os
import requests
import time

import params
import parser_utils

DATABASE_DIR = '../database/'

BASE_URL = 'http://comtrade.un.org/api/get?'

# check if database folder exist
def check_dependencies():
	if not os.path.exists(DATABASE_DIR):
	    os.makedirs(DATABASE_DIR)
	else:
		# if exists, remove all files inside
		for file in os.listdir(DATABASE_DIR):
			os.remove(DATABASE_DIR + file) 

def main():

	# params to change
	periods = '2015%2C2014%2C2014%2C2012%2C2011'
	reporters = 'all'
	partners = params.get_countries_urls()
	trade_flow = '1,2'
	classification_code = 'TOTAL'

	# always in groups of five or less
	number_of_calls = 0
	for partners_url in partners:
		params_url = ('max=50000' +
					'&type=C'+
					'&freq=A'+
					'&px=HS' +
					'&ps='+ periods +
					'&r='+ reporters +
					'&p=' + partners_url +
					'&rg=' + trade_flow +
					'&cc=' + classification_code +
					'&fmt=csv')
		
		# get request
		response = requests.get(BASE_URL + params_url)
		number_of_calls = number_of_calls + 1

		# write csv response
		file = open(DATABASE_DIR + "comtrade_{}.csv".format(number_of_calls),"w")
		file.write(response.content)
		file.close() 

		# wait one second to make another api get
		time.sleep(1)

		# wait one hour if number of requests exceed limit per hour
		if(number_of_calls == 100):
			time.sleep(3600)

	
if __name__ == '__main__':
	
	# check if all folders are all right
	check_dependencies()

	# call API
	main()

	# create result file
	parser_utils.parse_results()
