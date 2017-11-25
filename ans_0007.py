import os

def readFile(filepath):
	f = open(filepath, 'r')
	whiteSpaceLineCount = 0
	markLineCount = 0
	codeLineCount = 0

	for line in f:
		if line == '\n':
			whiteSpaceLineCount += 1
		elif line.startswith('#'):
			markLineCount += 1
		else:
			codeLineCount += 1
	return (whiteSpaceLineCount, markLineCount, codeLineCount)

if __name__ == '__main__':
	path = '.'
	(totalWhiteSpaceLineCount, totalMarkLineCount, totalCodeLineCount) = (0, 0, 0)

	for root, dirs, files in os.walk(path):
		for file in files:
			filepath = path + '/' + file
			if filepath.endswith('.py'):
				(whiteSpaceLineCount, markLineCount, codeLineCount)  = readFile(filepath)
				totalWhiteSpaceLineCount += whiteSpaceLineCount
				totalMarkLineCount += markLineCount
				totalCodeLineCount += codeLineCount

	print("------------------")
	print("totalWhiteSpaceLineCount:" + str(totalWhiteSpaceLineCount))
	print("totalMarkLineCount:" + str(totalMarkLineCount))
	print("totalCodeLineCount:" + str(totalCodeLineCount))