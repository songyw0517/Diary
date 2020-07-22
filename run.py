import sys
sys.path.insert(0,'./')
sys.path.insert(0,'./DB')
sys.path.insert(0,'./app')
from flask import Flask, url_for, render_template, request
from flask import request
from init_database import *


import main

app = Flask(__name__, instance_relative_config=True)
def main_app():
    #DB초기화
    init_db()

    #blueprint 등록
    app.register_blueprint(main.BP) # 오류아님, 잘 작동됨

@app.before_request
def before_request():
    get_db()

@app.teardown_request
def teardown_request(exception):
    close_db()

if __name__ == '__main__':
    main_app()
    app.run(host="127.0.0.1", debug=True)