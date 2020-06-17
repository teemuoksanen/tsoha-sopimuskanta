from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from application import app, db, bcrypt, login_required
from application.auth.models import User
from application.auth.forms import LoginForm, UserForm, UserEditForm, UserOwnSettingsForm, PasswordEditForm

@app.route("/users/", methods=["GET"])
@login_required(role="ADMIN")
def users_index():
    users = User.users_with_contracts_count()
    return render_template("auth/list.html", users = users)

@app.route("/users/new/", methods=["POST"])
@login_required(role="ADMIN")
def users_create():
    form = UserForm(request.form)

    if not form.validate():
        return render_template("auth/new.html", form = form)

    pw_hash = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user = User(form.name.data, form.username.data, pw_hash, form.user_role.data)

    db.session().add(user)
    db.session().commit()
  
    return redirect(url_for("users_index"))

@app.route("/users/new/", methods=["GET"])
@login_required(role="ADMIN")
def users_new():
    return render_template("auth/new.html", form = UserForm())

@app.route("/users/edit/<int:user_id>/", methods=["GET"])
@login_required(role="ADMIN")
def users_edit_form(user_id):
    user = User.query.get_or_404(user_id)
    form = UserEditForm(obj=user)
    form_pw = PasswordEditForm(obj=user)
    return render_template("auth/edit.html", form = form, form_pw = form_pw, user = user, updated = "none")

@app.route("/users/edit/<int:user_id>/", methods=["POST"])
@login_required(role="ADMIN")
def users_edit(user_id):
    user = User.query.get_or_404(user_id)
    form = UserEditForm(request.form)
    form.current_username.data = user.username
    form_pw = PasswordEditForm(obj=user)

    if not form.validate():
        return render_template("auth/edit.html", form = form, form_pw = form_pw, user = user, updated = "none")

    user.username = form.username.data
    user.name = form.name.data
    user.user_role = form.user_role.data

    db.session().add(user)
    db.session().commit()

    return render_template("auth/edit.html", form = form, form_pw = form_pw, user = user, updated = "user")

@app.route("/users/edit/<int:user_id>/password/", methods=["POST"])
@login_required(role="ADMIN")
def users_edit_pw(user_id):
    user = User.query.get_or_404(user_id)
    form = UserEditForm(obj=user)
    form_pw = PasswordEditForm(request.form)

    if not form_pw.validate():
        return render_template("auth/edit.html", form = form, form_pw = form_pw, user = user, updated = "none")

    pw_hash = bcrypt.generate_password_hash(form_pw.password.data).decode('utf-8')
    user.password = pw_hash

    db.session().add(user)
    db.session().commit()

    return render_template("auth/edit.html", form = form, form_pw = form_pw, user = user, updated = "pw")

@app.route("/settings/", methods=["GET"])
@login_required(role="ANY")
def own_settings_form():
    user = current_user
    form = UserOwnSettingsForm(obj=user)
    form_pw = PasswordEditForm(obj=user)
    return render_template("auth/ownsettings.html", form = form, form_pw = form_pw, updated = "none")

@app.route("/settings/", methods=["POST"])
@login_required(role="ANY")
def own_settings():
    user = current_user
    form = UserOwnSettingsForm(request.form)
    form.current_username.data = user.username
    form_pw = PasswordEditForm(obj=user)

    if not form.validate():
        return render_template("auth/ownsettings.html", form = form, form_pw = form_pw, updated = "none")

    user.username = form.username.data
    user.name = form.name.data

    db.session().add(user)
    db.session().commit()

    return render_template("auth/ownsettings.html", form = form, form_pw = form_pw, updated = "user")

@app.route("/settings/password/", methods=["POST"])
@login_required(role="ANY")
def own_settings_pw():
    user = current_user
    form = UserEditForm(obj=user)
    form_pw = PasswordEditForm(request.form)

    if not form_pw.validate():
        return render_template("auth/ownsettings.html", form = form, form_pw = form_pw, updated = "none")

    pw_hash = bcrypt.generate_password_hash(form_pw.password.data).decode('utf-8')
    user.password = pw_hash

    db.session().add(user)
    db.session().commit()

    return render_template("auth/ownsettings.html", form = form, form_pw = form_pw, updated = "pw")

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        form = LoginForm()
        form.nextpage.data = request.args.get('next')
        return render_template("auth/loginform.html", form = form)

    form = LoginForm(request.form)

    user = User.query.filter_by(username=form.username.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "Käyttäjää ei löytynyt!")

    if not bcrypt.check_password_hash(user.password, form.password.data):
        return render_template("auth/loginform.html", form = form,
                               error = "Salasana oli virheellinen!")

    login_user(user)

    if request.form.get("nextpage"):
        return redirect(request.form.get("nextpage"))
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))  