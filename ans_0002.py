
import pymysql
import ans_0001


# create database pytest
db = pymysql.connect("localhost", "root", "880404")
cursor = db.cursor()

cursor.execute("DROP DATABASE IF EXISTS pytest")
cursor.execute("CREATE DATABASE IF NOT EXISTS pytest")

db.commit()
db.close()

# create table tbcode
db = pymysql.connect("localhost", "root", "880404", "pytest")
cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS tb_codes")

sql = """CREATE TABLE tb_codes(
			id Int PRIMARY KEY AUTO_INCREMENT,
			code char(20))"""
cursor.execute(sql)

# insert codes to tb_codes
codes = ans_0001.getCodes()
for code in codes:
	sql = "insert into tb_codes(code) values('%s')" % (code)
	try:
		cursor.execute(sql)
		db.commit()
	except:
		db.rollback()
#print(ans_0001.getCodes())

db.close()