from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///contracts.db"
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# Login
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager, current_user
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Sinun on kirjauduttava sisään käyttääksesi tätä toimintoa."

# roles in login_required
from functools import wraps

def login_required(_func=None, *, role="ANY"):
    def wrapper(func):
        @wraps(func)
        def decorated_view(*args, **kwargs):
            if not (current_user and current_user.is_authenticated):
                return login_manager.unauthorized()

            acceptable_roles = set(("ANY", *current_user.roles()))

            if role not in acceptable_roles:
                return login_manager.unauthorized()

            return func(*args, **kwargs)
        return decorated_view
    return wrapper if _func is None else wrapper(_func)

from application import views

# Contracts
from application.contracts import models
from application.contracts import views

# Parties
from application.parties import models
from application.parties import views

# Reminders
from application.reminders import models
from application.reminders import views

# Users
from application.auth import models
from application.auth import views

# Login, part 2
from application.auth.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

try:
    db.create_all()
    stmt = text("INSERT INTO account (id, name, username, password, user_role)"
                " VALUES (1, 'Testikäyttäjä', 'testi',"
                " '$2b$12$uXCpc8Fz3BdzOZiYqIUdn.wIhqyzwICpag0K4XnUPYUhWKlKymjz2', 'ADMIN')")
    db.engine.execute(stmt)
except:
    pass
