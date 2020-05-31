from application import app, db
from flask_login import login_required, current_user

from flask import redirect, render_template, request, url_for
from datetime import date
from application.contracts.models import Contract
from application.contracts.forms import ContractForm, ContractPartyForm
from application.parties.models import Party

@app.route("/contracts/", methods=["GET"])
def contracts_index():
    return render_template("contracts/list.html", contracts = Contract.query.all())

@app.route("/contracts/", methods=["POST"])
@login_required
def contracts_create():
    form = ContractForm(request.form)

    if not form.validate():
        return render_template("contracts/form.html", form = form, action = "new")

    contract = Contract(form.name.data)
    contract.date_signed = form.date_signed.data
    contract.date_entry = form.date_entry.data
    contract.date_expiry = form.date_expiry.data
    contract.account_id = current_user.id

    db.session().add(contract)
    db.session().commit()
  
    return redirect(url_for("contracts_index"))

@app.route("/contracts/new/")
@login_required
def contracts_new():
    form = ContractForm()
    return render_template("contracts/form.html", form = form)

@app.route("/contracts/<int:contract_id>/", methods=["GET"])
@login_required
def contracts_view(contract_id):
    contract = Contract.query.get(contract_id)
    form = ContractPartyForm()
    form.parties.choices = Contract.parties_not_linked_to_contract(contract_id=contract_id)
    form.parties.choices.insert(0, (0, "-- Valitse osapuoli --"))
    return render_template("contracts/view.html", contract = contract, form = form, today = date.today(), addPartyError = 0)

@app.route("/contracts/delete/<contract_id>/", methods=["POST"])
@login_required
def contracts_delete(contract_id):

    contract = Contract.query.get(contract_id)

    db.session().delete(contract)
    db.session().commit()

    return redirect(url_for("contracts_index"))

@app.route("/contracts/edit/<int:contract_id>/", methods=["GET"])
@login_required
def contracts_edit_form(contract_id):
    contract = Contract.query.get(contract_id)
    form = ContractForm(obj=contract)
    return render_template("contracts/form.html", form = form, action = "edit", contract_id = contract_id)

@app.route("/contracts/edit/<int:contract_id>/", methods=["POST"])
@login_required
def contracts_edit(contract_id):
    form = ContractForm(request.form)

    if not form.validate():
        return render_template("contracts/form.html", form = form, action = "edit")

    editedContract = Contract.query.get(contract_id)
    editedContract.name = form.name.data
    editedContract.date_signed = form.date_signed.data
    editedContract.date_entry = form.date_entry.data
    editedContract.date_expiry = form.date_expiry.data

    db.session().add(editedContract)
    db.session().commit()
  
    return redirect(url_for('contracts_view', contract_id=contract_id))

@app.route("/contracts/<int:contract_id>/", methods=["POST"])
@login_required
def contracts_addparty(contract_id):
    contract = Contract.query.get(contract_id)
    form = ContractPartyForm(request.form)
    form.parties.choices = [(party.id, party.name) for party in Party.query.order_by('name').all()]
    form.parties.choices.insert(0, (0, "-- Valitse osapuoli --"))

    if not form.validate():
        return render_template("contracts/view.html", contract = contract, form = form, today = date.today(), addPartyError = 1)
    
    contract.parties.append(Party.query.get(form.parties.data))
    
    db.session().add(contract)
    db.session().commit()
            
    return redirect(url_for('contracts_view', contract_id=contract_id))

@app.route("/contracts/<int:contract_id>/removeparty/<int:party_id>/", methods=["GET"])
@login_required
def contracts_removeparty(contract_id, party_id):
    contract = Contract.query.get(contract_id)
    form = ContractPartyForm()
    party = Party.query.get(party_id)

    if not party:
        return render_template("contracts/view.html", contract = contract, form = form, today = date.today(), addPartyError = 1)
    
    contract.parties.remove(party)
    
    db.session().add(contract)
    db.session().commit()
            
    return redirect(url_for('contracts_view', contract_id=contract_id))

    return render_template("contracts/view.html", contract = contract, form = form, today = date.today(), addPartyError = 0)