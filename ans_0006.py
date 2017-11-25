import os
import re

def findMostImportantWord(filepath):
	f = open(filepath, "r")
	wordsCount = {}
	for line in f:
		line = line.replace("\n", '')
		words = re.findall('[a-zA-Z0-9]+', line)

		# count every word of line
		for word in words:
			if word in wordsCount.keys():
				wordsCount[word] += 1
			else:
				wordsCount[word] = 1

	# find the most key
	mostCount = 0
	for key in wordsCount.keys():
		if wordsCount[key] > mostCount:
			mostCount = wordsCount[key]
	
	# print the most key
	for key in wordsCount.keys():
		if wordsCount[key] == mostCount:
			print(key + ":" + str(mostCount))

if __name__ == '__main__':
	path = "0006"
	for root, dirs, files in os.walk(path):
		for file in files:
			filepath = path + "/" + file
			findMostImportantWord(filepath)
			print('\n')