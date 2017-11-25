import re

if __name__ == '__main__':
	wordsCount = {}
	f = open('0004/0004.text', 'r')
	for line in f:
		line = line.replace('\n', '')
		# print(line)
		# words = line.split(' ')
		words = re.findall('[a-zA-Z0-9]+',line)

		for word in words:
			if word in wordsCount.keys():
				wordsCount[word] += 1
			else:
				wordsCount[word] = 1
	for key in wordsCount.keys():
		print(key+":"+str(wordsCount[key]))
