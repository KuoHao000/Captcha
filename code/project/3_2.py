from flask import Flask
import sql_helper

app = Flask(__name__)


@app.route('/login')
def login():
    result = sql_helper.fetchone('select * from user where user=%s', 'a')
    print(result)
    return 'login'


@app.route('/index')
def index():
    return


@app.route('/order')
def order():
    return


if __name__ == '__main__':
    app.run(debug=True)
