from flask import Flask
from sql_helper2 import db

app = Flask(__name__)
app.config.from_object('config.settings')


@app.route('/login')
def login():
    result = db.fetchone('select * from user where user=%s', 'a')
    print(result, db)
    return 'login'


@app.route('/index')
def index():
    result = db.fetchall('select * from user')
    print(result, db)
    return 'index'


@app.route('/order')
def order():
    return


if __name__ == '__main__':
    app.run(debug=True)
