from application import app, db, login_required
from flask_login import current_user

from flask import redirect, render_template, request, url_for
from datetime import date
from application.contracts.models import Contract
from application.contracts.forms import ContractForm, ContractPartyForm, ContractSearch
from application.parties.models import Party
from application.reminders.models import Reminder
from application.auth.models import User

@app.route("/contracts/", methods=["GET"])
@login_required(role="ANY")
def contracts_index():
    return render_template("contracts/list.html", contracts = Contract.query.all(), form = ContractSearch(), today = date.today())

@app.route("/contracts/", methods=["POST"])
@login_required(role="ANY")
def contracts_search():
    form = ContractSearch(request.form)
    form.search.data = form.search.data.strip()
    
    if not form.validate():
        return render_template("contracts/list.html", contracts = Contract.query.all(), form = form)
    
    return render_template("contracts/list.html", contracts = Contract.search(form.search.data, form.onlyOwn.data, form.onlyValid.data), form = form, today = date.today())

@app.route("/contracts/new/", methods=["POST"])
@login_required(role="ANY")
def contracts_create():
    form = ContractForm(request.form)
    form.account_id.choices = [(account.id, account.username+" ("+account.name+")") for account in User.query.order_by('username').all()]

    if not form.validate():
        return render_template("contracts/form.html", form = form, action = "new")

    contract = Contract(form.name.data)
    contract.date_signed = form.date_signed.data
    contract.date_entry = form.date_entry.data
    contract.date_expiry = form.date_expiry.data
    contract.account_id = form.account_id.data

    db.session().add(contract)
    db.session().commit()

    if contract.date_expiry:
        Reminder.create_expiry_reminder(contract)
  
    return redirect(url_for("contracts_view", contract_id = contract.id))

@app.route("/contracts/new/", methods=["GET"])
@login_required(role="ANY")
def contracts_new():
    form = ContractForm()
    if current_user.user_role == "ADMIN":
        form.account_id.choices = [(account.id, account.username+" ("+account.name+")") for account in User.query.order_by('username').all()]
    return render_template("contracts/form.html", form = form)

@app.route("/contracts/<int:contract_id>/", methods=["GET"])
@login_required(role="ANY")
def contracts_view(contract_id):
    contract = Contract.query.get_or_404(contract_id)
    form = ContractPartyForm()
    form.parties.choices = Contract.parties_not_linked_to_contract(contract_id=contract_id)
    return render_template("contracts/view.html", contract = contract, form = form, today = date.today(), addPartyError = 0)

@app.route("/contracts/delete/<contract_id>/", methods=["POST"])
@login_required(role="ANY")
def contracts_delete(contract_id):

    contract = Contract.query.get_or_404(contract_id)

    if not (contract.account_id == current_user.id or current_user.user_role == "ADMIN"):
        return redirect(url_for("contracts_view", contract_id = contract_id))

    db.session().delete(contract)
    db.session().commit()

    return redirect(url_for("contracts_index"))

@app.route("/contracts/edit/<int:contract_id>/", methods=["GET"])
@login_required(role="ANY")
def contracts_edit_form(contract_id):
    contract = Contract.query.get_or_404(contract_id)

    if not (contract.account_id == current_user.id or current_user.user_role == "ADMIN"):
        return redirect(url_for("contracts_view", contract_id = contract_id))
        
    form = ContractForm(obj=contract)
    if current_user.user_role == "ADMIN":
        form.account_id.choices = [(account.id, account.username+" ("+account.name+")") for account in User.query.order_by('username').all()]
    return render_template("contracts/form.html", form = form, action = "edit", contract_id = contract_id)

@app.route("/contracts/edit/<int:contract_id>/", methods=["POST"])
@login_required(role="ANY")
def contracts_edit(contract_id):
    editedContract = Contract.query.get_or_404(contract_id)
    form = ContractForm(request.form)
    form.account_id.choices = [(account.id, account.username+" ("+account.name+")") for account in User.query.order_by('username').all()]

    if form.date_expiry.data and (editedContract.date_expiry != form.date_expiry.data):
        update_expiry_reminder = True

    if not (editedContract.account_id == current_user.id or current_user.user_role == "ADMIN"):
        return redirect(url_for("contracts_view", contract_id = contract_id))

    if not form.validate():
        return render_template("contracts/form.html", form = form, action = "edit")

    editedContract.name = form.name.data
    editedContract.date_signed = form.date_signed.data
    editedContract.date_entry = form.date_entry.data
    editedContract.date_expiry = form.date_expiry.data
    editedContract.account_id = form.account_id.data

    db.session().add(editedContract)
    db.session().commit()

    if update_expiry_reminder:
        Reminder.create_expiry_reminder(editedContract)
  
    return redirect(url_for('contracts_view', contract_id=contract_id))

@app.route("/contracts/<int:contract_id>/", methods=["POST"])
@login_required(role="ANY")
def contracts_addparty(contract_id):
    contract = Contract.query.get_or_404(contract_id)

    if not (contract.account_id == current_user.id or current_user.user_role == "ADMIN"):
        return redirect(url_for("contracts_view", contract_id = contract_id))

    form = ContractPartyForm(request.form)
    form.parties.choices = [(party.id, party.name) for party in Party.query.order_by('name').all()]

    if not form.validate():
        return render_template("contracts/view.html", contract = contract, form = form, today = date.today(), addPartyError = 1)
    
    contract.parties.append(Party.query.get_or_404(form.parties.data))
    
    db.session().add(contract)
    db.session().commit()
            
    return redirect(url_for('contracts_view', contract_id=contract_id))

@app.route("/contracts/<int:contract_id>/removeparty/<int:party_id>/", methods=["GET"])
@login_required(role="ANY")
def contracts_removeparty(contract_id, party_id):
    contract = Contract.query.get_or_404(contract_id)

    if not (contract.account_id == current_user.id or current_user.user_role == "ADMIN"):
        return redirect(url_for("contracts_view", contract_id = contract_id))
        
    form = ContractPartyForm()
    party = Party.query.get_or_404(party_id)

    if not party:
        return render_template("contracts/view.html", contract = contract, form = form, today = date.today(), addPartyError = 1)
    
    contract.parties.remove(party)
    
    db.session().add(contract)
    db.session().commit()
            
    return redirect(url_for('contracts_view', contract_id=contract_id))

    return render_template("contracts/view.html", contract = contract, form = form, today = date.today(), addPartyError = 0)