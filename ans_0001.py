import random

def getCodes():
	codes = 'abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
	activationCode = []

	for i in range(0, 100):
	    code = random.sample(codes, 10)
	    str = ''.join(code)
	    activationCode.append(str)
	return activationCode

if __name__ =='__main__':
	print(getCodes())