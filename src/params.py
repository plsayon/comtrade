#!/usr/bin/python

import params_utils

COUNTRIES_LIST = '../utils/countries.txt'

def get_countries_urls():
	
	countries = []
	file = open(COUNTRIES_LIST, "r")
	
	for country in file:
		countries.append(params_utils.get_country_id(country.rstrip('\n')));

	count = 1
	aux = []
	urls = []
	for country in countries:
		aux.append(country)
		if count % 5 == 0 or count == len(countries):
			urls.append(params_utils.get_url_multiple_items(aux))
			aux = []

		count = count + 1

	return urls