import redis
import ans_0001

if __name__ == '__main__':
	r = redis.Redis(host='localhost', port=6379, db=0)
	codes = ans_0001.getCodes()
	r.set("codes", codes)
	print(r.get('codes'))