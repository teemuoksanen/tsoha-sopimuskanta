from application import app, db
from flask_login import login_required

from flask import redirect, render_template, request, url_for
from application.contracts.models import Contract
from application.contracts.forms import ContractForm

@app.route("/contracts", methods=["GET"])
def contracts_index():
    return render_template("contracts/list.html", contracts = Contract.query.all())

@app.route("/contracts/new/")
@login_required
def contracts_form():
    return render_template("contracts/new.html", form = ContractForm())

@app.route("/contracts/", methods=["POST"])
@login_required
def contracts_create():
    form = ContractForm(request.form)

    if not form.validate():
        return render_template("contracts/new.html", form = form)

    contract = Contract(form.name.data)

    db.session().add(contract)
    db.session().commit()
  
    return redirect(url_for("contracts_index"))