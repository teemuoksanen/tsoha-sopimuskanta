from application import app, db
from flask_login import login_required, current_user

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
    contract.date_signed = form.date_signed.data
    contract.date_entry = form.date_entry.data
    contract.date_expiry = form.date_expiry.data
    contract.account_id = current_user.id

    db.session().add(contract)
    db.session().commit()
  
    return redirect(url_for("contracts_index"))

@app.route("/contracts/delete/<contract_id>/", methods=["POST"])
@login_required
def contracts_delete(contract_id):

    contract = Contract.query.get(contract_id)

    db.session().delete(contract)
    db.session().commit()

    return redirect(url_for("contracts_index"))