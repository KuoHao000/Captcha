from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views',__name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html", user=current_user)

@views.route('/userinterface', methods=['GET', 'POST'])
@login_required
def userinterface():
    return render_template("userinterface.html", user=current_user)

@views.route('/choice', methods=['GET', 'POST'])
@login_required
def choice():
    return render_template("choice.html", user=current_user)

