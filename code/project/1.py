from flask import Flask

app = Flask(__name__)

@app.route('/')
def login():
    return '登入'

if __name__ == '__main__':
    app.run()