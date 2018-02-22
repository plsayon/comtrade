#!/usr/bin/python

import requests

BASE_URL = 'http://comtrade.un.org/api/get?'
PARAMS = 'max=500&type=C&freq=A&px=HS&ps=2017&r=all&p=76%2C4%2C8%2C818%2C70&rg=2&cc=TOTAL&fmt=csv'

def main():
	headers = requests.utils.default_headers()
	headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'
	
	response = requests.get(BASE_URL + PARAMS, headers=headers)
	# .decode('utf-8')
	
	file = open("response.csv","w")
	file.write(response.content)
	file.close() 
	
if __name__ == '__main__':
	main()