from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from flask_login import current_user

from application.reminders.models import Reminder
from application.reminders.forms import ReminderForm
from application.contracts.models import Contract
from application.auth.models import User

@app.route("/reminders/", methods=["GET"])
@login_required(role="ANY")
def reminders_index():
    return render_template("reminders/list.html", undone_reminders = Reminder.undone_reminders_for_user(current_user.id), done_reminders = Reminder.done_reminders_for_user(current_user.id), all = False)

@app.route("/reminders/all/", methods=["GET"])
@login_required(role="ADMIN")
def reminders_all():
    return render_template("reminders/list.html", undone_reminders = Reminder.all_undone_reminders(), done_reminders = Reminder.all_done_reminders(), all = True)

@app.route("/reminders/new/", methods=["POST"])
@login_required(role="ANY")
def reminders_create():
    form = ReminderForm(request.form)
    form.account_id.choices = [(account.id, account.username+" ("+account.name+")") for account in User.query.order_by('username').all()]
    form.contract_id.choices = [(contract.id, contract.name) for contract in Contract.query.order_by('name').all()]

    if not form.validate():
        return render_template("reminders/form.html", form = form)
    
    reminder = Reminder(form.note.data)
    reminder.date_remind = form.date_remind.data
    reminder.contract_id = form.contract_id.data

    if current_user.user_role == "ADMIN":
        reminder.account_id = form.account_id.data
    else:
        reminder.account_id = current_user.id
    reminder.done = False

    db.session().add(reminder)
    db.session().commit()
  
    return redirect(url_for("reminders_index"))

@app.route("/reminders/new/", methods=["GET"])
@login_required(role="ANY")
def reminders_new():
    form = ReminderForm()
    form.contract_id.choices = [(contract.id, contract.name) for contract in Contract.query.order_by('name').all()]
    if current_user.user_role == "ADMIN":
        form.account_id.choices = [(account.id, account.username+" ("+account.name+")") for account in User.query.order_by('username').all()]
    return render_template("reminders/form.html", form = form)

@app.route("/reminders/new/<int:contract_id>/", methods=["GET"])
@login_required(role="ANY")
def reminders_new_for_contract(contract_id=0):
    form = ReminderForm()
    form.contract_id.data = contract_id
    form.contract_id.choices = [(contract.id, contract.name) for contract in Contract.query.order_by('name').all()]
    form.account_id.choices = [(account.id, account.username+" ("+account.name+")") for account in User.query.order_by('username').all()]
    return render_template("reminders/form.html", form = form)

@app.route("/reminders/delete/<reminder_id>/", methods=["POST"])
@login_required(role="ANY")
def reminders_delete(reminder_id):

    reminder = Reminder.query.get(reminder_id)

    if not (reminder.account_id == current_user.id or current_user.user_role == "ADMIN"):
        return redirect(url_for("reminders_index"))

    db.session().delete(reminder)
    db.session().commit()

    return redirect(url_for("reminders_index"))

@app.route("/reminders/edit/<int:reminder_id>/", methods=["GET"])
@login_required(role="ANY")
def reminders_edit_form(reminder_id):
    reminder = Reminder.query.get(reminder_id)

    if not (reminder.account_id == current_user.id or current_user.user_role == "ADMIN"):
        return redirect(url_for("reminders_index"))

    form = ReminderForm(obj=reminder)
    form.contract_id.choices = [(contract.id, contract.name) for contract in Contract.query.order_by('name').all()]
    form.account_id.choices = [(account.id, account.username+" ("+account.name+")") for account in User.query.order_by('username').all()]
    return render_template("reminders/form.html", form = form, action = "edit", reminder_id = reminder_id)

@app.route("/reminders/edit/<int:reminder_id>/", methods=["POST"])
@login_required(role="ANY")
def reminders_edit(reminder_id):
    editedReminder = Reminder.query.get(reminder_id)

    if not (editedReminder.account_id == current_user.id or current_user.user_role == "ADMIN"):
        return redirect(url_for("reminders_index"))

    form = ReminderForm(request.form)
    form.contract_id.choices = [(contract.id, contract.name) for contract in Contract.query.order_by('name').all()]
    form.account_id.choices = [(account.id, account.username+" ("+account.name+")") for account in User.query.order_by('username').all()]

    if not form.validate():
        return render_template("reminders/form.html", form = form, action = "edit", reminder_id = reminder_id)

    editedReminder.note = form.note.data
    editedReminder.date_remind = form.date_remind.data
    editedReminder.contract_id = form.contract_id.data
    editedReminder.account_id = form.account_id.data

    db.session().add(editedReminder)
    db.session().commit()
  
    return redirect(url_for('reminders_index'))

@app.route("/reminders/<int:reminder_id>/setdone/", methods=["POST"])
@login_required(role="ANY")
def reminders_set_done(reminder_id):

    reminder = Reminder.query.get(reminder_id)

    if not (reminder.account_id == current_user.id or current_user.user_role == "ADMIN"):
        return redirect(url_for("reminders_index"))

    reminder.done = True
    db.session().commit()

    if request.form.get('origin') == "True":
        return redirect(url_for('reminders_all'))
    elif request.form.get('origin') == "index":
        return redirect(url_for('index'))
    else:
        return redirect(url_for('reminders_index'))

@app.route("/reminders/<int:reminder_id>/unsetdone/", methods=["POST"])
@login_required(role="ANY")
def reminders_unset_done(reminder_id):

    reminder = Reminder.query.get(reminder_id)

    if not (reminder.account_id == current_user.id or current_user.user_role == "ADMIN"):
        return redirect(url_for("reminders_index"))
        
    reminder.done = False
    db.session().commit()

    if request.form.get('all') == "True":
        return redirect(url_for('reminders_all'))

    return redirect(url_for('reminders_index'))