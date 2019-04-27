
import pymysql
import random
import string


def cdkey(num):
    s = set()
    while len(s) < num:
        code = random.sample(string.ascii_uppercase + string.digits, 6)
        s.add(''.join(code))
    return s






conn = pymysql.connect("localhost", "root", "95219521", "CDKEYdb")
cursor = conn.cursor()

sql = """
CREATE TABLE IF NOT EXISTS CDKEY(
id INT ,
num CHAR(20) NOT NULL UNIQUE
)ENGINE = innodb DEFAULT CHARSET = utf8;

"""
# cursor.execute("DROP TABLE IF EXISTS USER1")
cursor.execute(sql)

cdkey_list = sorted(list(cdkey(200)))

for i, num in enumerate(cdkey_list):
    sql = """
    INSERT INTO CDKEY value(%s,'%s')
    """ % (i, str(num))
    cursor.execute(sql)

cursor.close()
conn.commit()
conn.close()