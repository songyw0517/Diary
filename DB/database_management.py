from flask import request
import pymysql

def login_validation(db, value):
    with db.cursor() as cursor:
        query = "SELECT ID FROM test_login WHERE ID=%s and PW=%s"
        cursor.execute(query, value)
        data = (cursor.fetchall())
        cursor.close()
        for row in data:
            data = row[0]
        if data:
            print("성공")
        else:
            print("실패")
