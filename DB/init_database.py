import pymysql
from flask import g
#########################
DB_IP = 'localhost'
DB_ID = 'root'
DB_PW = 'root'
DB_Name = 'scof'

#########################
def get_db():
    if 'db' not in g:
        g.db = pymysql.connect(host=DB_IP, user=DB_ID, password=DB_PW, db=DB_Name, charset='utf8')

def close_db():
    db = g.pop('db', None)
    if db is not None:
        if db.open:
            db.close()


def init_db(): # http://pythonstudy.xyz/python/article/202-MySQL-%EC%BF%BC%EB%A6%AC
    # MySQL Connection 연결
    db = pymysql.connect(host='localhost', user='root', password='root', db='scof', charset='utf8')

    # Connection 으로부터 Cursor 생성
    curs = db.cursor()

    #SQL문 실행
    sql = 'SELECT * FROM test_login'
    curs.execute(sql)

    # 데이터 fetch ?
    rows = curs.fetchall()
    print(rows)

    db.close()