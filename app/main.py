from flask import Blueprint, render_template, g, request
from DB import database_management as DBM
BP = Blueprint('main', __name__)

@BP.route('/')
def home():
    return render_template('index.html')

@BP.route('/login', methods=['POST', 'GET'])
def login():
    id = request.form['id']
    pw = request.form['pw']
    value = (id, pw)
    result = DBM.login_validation(g.db, value)
    return render_template('index.html', msg=result)