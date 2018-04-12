#!/usr/bin/python

import os

DATABASE_DIR = '../database/'

def parse_results():
	# if result.csv exists, delete it
	if(os.path.exists("{}result.csv".format(DATABASE_DIR))):
		os.remove("{}result.csv".format(DATABASE_DIR))

	for file in os.listdir(DATABASE_DIR):
		with open("{}result.csv".format(DATABASE_DIR), "a") as result_file:
			with open(DATABASE_DIR + file, "r") as comtrade_file:

				# start in the second line
				if(file != "comtrade_1.csv"):
					next(comtrade_file)

				# read file and append in result_file
				for line in comtrade_file:
				    result_file.write(line)

				# close comtrade file
				comtrade_file.close()

			# close result file
			result_file.close()
