from flask import Flask, url_for, render_template, request
from flask import request

app = Flask(__name__)
from markupsafe import escape
@app.route('/')
def helloWorld(name=None):
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="127.0.0.1", debug=True)