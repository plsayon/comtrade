#!/usr/bin/python

import os
import requests

DATABASE_DIR = '../database/'

BASE_URL = 'http://comtrade.un.org/api/get?'

PERIODS = '2017%2C2016%2C2015'
REPORTERS = 'all'
PARTNERS = '76%2C4%2C8%2C818%2C70'
TRADE_FLOW = '2' # 2 - export 1 - import 
CLASSIFICATION_CODE = 'TOTAL'
PARAMS = 'max=50000&type=C&freq=A&px=HS&ps={}&r={}&p={}&rg={}&cc={}&fmt=csv'.format(PERIODS, REPORTERS, PARTNERS, TRADE_FLOW, CLASSIFICATION_CODE)

def check_dependencies():
	if not os.path.exists(DATABASE_DIR):
	    os.makedirs(DATABASE_DIR)

def main():
	response = requests.get(BASE_URL + PARAMS)
	
	file = open(DATABASE_DIR + "response.csv","w")
	file.write(response.content)
	file.close() 
	
if __name__ == '__main__':
	check_dependencies()
	main()