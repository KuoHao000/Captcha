from flask import Flask, request, redirect, render_template
from flask.views import View
from sql_helper2 import User, Users, db
from mail import sendmail

app = Flask(__name__)


class Index(View):
    def dispatch_request(self):
        return render_template('index.html')


app.add_url_rule('/index',
                 view_func=Index.as_view('index'))


class Register(View):
    def dispatch_request(self):
        if request.method == 'GET':
            return render_template('register.html')
        elif request.method == 'POST':
            name = request.form['name']
            password = request.form['password']
            password_check = request.form['password_check']
            email = request.form['email']

            sql = "INSERT INTO user (user, password, email) VALUES (%s, %s, %s)"
            args = (name, password, email)

            db.insert(sql, *args)

            url = email

            sendmail(email, url)

            return redirect('index')


app.add_url_rule('/register',
                 view_func=Register.as_view('register'), methods=['GET', 'POST'])


class ListView(View):
    def __init__(self, model, templates):
        self.model = model
        self.templates = templates

    def dispatch_request(self):
        result = self.model
        result = list(result)
        print(result)
        return render_template(self.templates, result=result)


app.add_url_rule('/user',
                 view_func=ListView.as_view('user', User, 'userInfo.html'))
app.add_url_rule('/users',
                 view_func=ListView.as_view('users', Users, 'usersInfo.html'))

# class ListView(View):
#     def __init__(self, model):
#         self.model = model
#
#     def dispatch_request(self):
#         return self.model
#
#
# app.add_url_rule('/index', view_func=ListView.as_view('index', 'indext'))
# app.add_url_rule('/login', view_func=ListView.as_view('login', 'logint'))

# class IndexView(View):
#     def dispatch_request(self):
#         result = db.fetchall('select * from user')
#         result = list(result)
#         return result
#
#
# app.add_url_rule('/index', view_func=IndexView.as_view(''))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
