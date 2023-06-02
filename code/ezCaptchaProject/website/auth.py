from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    # data = request.form
    # print(data)
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        print(user) 
        if user:
            if check_password_hash(user.password, password):
                print('success')
                flash('登入成功', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.userinterface'))
            else:
                print('error')
                flash('登入失敗', category='error')
        else:
            print('not')
            flash('Email 不存在')
        
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user() #登出
    return redirect(url_for('auth.login'))
 
@auth.route('/signup', methods=['GET', 'POST'])
def singup():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        passwordCheck = request.form.get('passwordCheck')

        user = User.query.filter_by(email=email).first()
        print(user)
        
        if user:
            flash('Email 已經存在', category='error')
        elif len(email) < 10:
            flash('Email to short, must greater than 10 character', category='error')
        elif len(name) < 5:
            flash('name to short, must greater than 5 character', category='error')
        elif password != passwordCheck:
            flash('Password not same', category='error')
        elif len(password) < 7:
            flash('Password must greater than 7 character', category='error')
        else:
            #add to DB
            new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            # login_user(user, remember=True)
            flash('Account Add Success', category='success')
            return redirect(url_for('views.home'))

    return render_template("signup.html", user=current_user)