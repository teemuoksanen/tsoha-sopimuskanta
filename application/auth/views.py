from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db, bcrypt
from application.auth.models import User
from application.auth.forms import LoginForm, UserForm

@app.route("/users", methods=["GET"])
@login_required
def users_index():
    return render_template("auth/list.html", users = User.query.all())

@app.route("/users/new/")
def users_form():
    return render_template("auth/new.html", form = UserForm())

@app.route("/users/", methods=["POST"])
def users_create():
    form = UserForm(request.form)

    if not form.validate():
        return render_template("auth/new.html", form = form)

    pw_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user = User(form.name.data, form.username.data, pw_hash)

    db.session().add(user)
    db.session().commit()
  
    return redirect(url_for("users_index"))

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "Käyttäjää ei löytynyt!")

    if not bcrypt.check_password_hash(user.password, form.password.data):
        return render_template("auth/loginform.html", form = form,
                               error = "Salasana oli virheellinen!")

    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))  