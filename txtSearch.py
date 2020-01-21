#!/bin/python
# txtSearch.py

# This is a text file (.txt) regex parser.
# User input and wil be required to specify the desired pattern. 

import sys, os, re, pyperclip, time

while True:
	try:
		fileToScan = sys.argv[1]
		break
	except IndexError:
		print('ERROR: Please provide a file as an argument: python txtSearch.py [text file]')
		sys.exit()

today = time.localtime()

def intro():
	print(" Today's time: ".rjust(20,'*') + str(time.strftime('%X', today) + ' '.ljust(15,'*')))
	print('\nWelcome to the text file regex parser. Please use like so: python txtSearch.py [text file]')

def fileCheck(fileToScan):
	try:
		fileObject = open(fileToScan, 'r') # Creating a fileObject after reading the scanned text file
	except FileNotFoundError:
		print('\nCould not find the file you typed: ' + str(sys.argv[1]))
		sys.exit()
	desiredPattern = re.compile(input('''\nPlease type a regex expression to search on. # Inputting the desired regex search pattern
		\nFor example the following regex: [a-z].* '''))
	matchObject = desiredPattern.search(fileObject.read()) # Match object created from reading the text file object
	try:
		print(matchObject.group())
	except AttributeError:
		print('Could not find a matched pattern in the file!')
	return

if __name__ == "__main__":
	intro()
	fileCheck(fileToScan)
