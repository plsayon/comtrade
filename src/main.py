#!/usr/bin/python

import os
import requests
import time

import params

DATABASE_DIR = '../database/'

BASE_URL = 'http://comtrade.un.org/api/get?'

# check if database folder exist
def check_dependencies():
	if not os.path.exists(DATABASE_DIR):
	    os.makedirs(DATABASE_DIR)

def main():

	# params to change
	periods = '2017%2C2016%2C2015'
	reporters = 'all'
	partners = params.get_countries_urls()
	trade_flow = '2'
	classification_code = 'TOTAL'

	# always in groups of five or less
	number_of_calls = 0
	for partners_url in partners:
		params_url = 'max=50000&type=C&freq=A&px=HS&ps={}&r={}&p={}&rg={}&cc={}&fmt=csv'.format(periods, reporters, partners_url, trade_flow, classification_code)
		
		# get request
		response = requests.get(BASE_URL + params_url)
		number_of_calls = number_of_calls + 1

		# write csv response
		file = open(DATABASE_DIR + "comtrade_{}.csv".format(number_of_calls),"w")
		file.write(response.content)
		file.close() 

		# wait one second to make another api get
		time.sleep(1) 

	
	
if __name__ == '__main__':
	check_dependencies()
	main()