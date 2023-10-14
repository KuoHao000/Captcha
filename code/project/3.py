from flask import Flask
import pymysql

app = Flask(__name__)

conn = pymysql.connect(host='192.168.158.128', port=3306, user='root', passwd='1o3g; 284', db='project')


def fetchall(sql):
    cursor = conn.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()

    return result


@app.route('/login')
def login():
    result = fetchall('select * from user')

    return 'login'


@app.route('/index')
def index():
    return


@app.route('/order')
def order():
    return


if __name__ == '__main__':
    app.run(debug=True)
