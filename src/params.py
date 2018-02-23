#!/usr/bin/python

import json

COUNTRIES_JSON = '../utils/countries.json'

def get_country_id(country_name):
	file = open(COUNTRIES_JSON, "r")
	data = json.load(file)

	for country in data['results']:
		 if country_name == country['text']:
			 return country['id']

def get_url_multiple_items(items):
	result_url = ""

	for item in items:
		result_url = result_url + item + "%2C"

	return result_url[:-3]