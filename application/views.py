from flask import render_template
from application import app
from flask_login import current_user

from application.reminders.models import Reminder
from application.auth.models import User

@app.route("/")
def index():
    if current_user.is_authenticated:
        active_reminders = Reminder.active_reminders_for_user(current_user.id)
    else:
        active_reminders = None
    return render_template("index.html", active_reminders = active_reminders)
