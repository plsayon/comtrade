#!/usr/bin/python

import os
import random
import requests
from time import sleep

import params
import parser_utils

DATABASE_DIR = '../database/'

BASE_URL = 'http://comtrade.un.org/api/get?'

# check if database folder exists
def check_dependencies():
	if not os.path.exists(DATABASE_DIR):
		os.makedirs(DATABASE_DIR)
	else:
		# if it exists and previous attempt was successful, remove all files inside
		if os.path.exists(DATABASE_DIR + "result.csv"):
			for file in os.listdir(DATABASE_DIR):
				print("Deleting" + " " + file)
				os.remove(DATABASE_DIR + file)

def main():

	# params to change
	periods = params.get_periods_urls()
	reporters = params.get_reporters_urls()
	partners = params.get_partners_urls()
	trade_flow = '2'
	classification_code = 'AG4'

	# always in groups of five or less
	number_of_calls = 0
	for periods_url in periods:
		for reporters_url in reporters:
			for partners_url in partners:					
				params_url = ('max=50000' +
							  '&type=C' +
							  '&freq=A' +
						  	  '&px=H3' +
						  	  '&ps=' + periods_url +
						  	  '&r=' + reporters_url +
						  	  '&p=' + partners_url +
						  	  '&rg=' + trade_flow +
						  	  '&cc=' + classification_code +
						  	  '&fmt=csv')

				number_of_calls = number_of_calls + 1

				#if previous attempt was unsuccessful, continues from where it stopped
				if os.path.exists(DATABASE_DIR + "comtrade_{}.csv".format(number_of_calls)):
					continue

				# get request
				response = requests.get(BASE_URL + params_url)

				# write csv response
				file = open(DATABASE_DIR + "comtrade_{}.csv".format(number_of_calls),"wb")
				file.write(response.content)
				file.close()

				# wait one second to make another api get
				sleep(random.uniform(1,10))

				# wait one hour if number of requests exceed limit per hour
				# if(number_of_calls % 100 == 0):
					# sleep(3500)

	
if __name__ == '__main__':
	
	# check if all folders are all right
	check_dependencies()

	# call API
	main()

	# create result file
	parser_utils.parse_results()
