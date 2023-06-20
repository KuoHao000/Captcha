from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

import pymysql
pymysql.install_as_MySQLdb()

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'test'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://test/1o3g; 284@127.0.0.1:3306/t'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://user:1o3g; 284@db/ezcaptcha'
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User

    with app.app_context():
        db.create_all()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
    return app
