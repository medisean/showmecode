import random
codes = 'abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

activationCode = []

for i in range(0, 100):
    code = random.sample(codes, 10)
    str = ''.join(code)
    print(str)
