from application import app, db, login_required
from flask import redirect, render_template, request, url_for
from datetime import date
from flask_login import current_user

from application.parties.models import Party
from application.parties.forms import PartyForm, PartySearch
from application.reminders.models import Reminder

@app.route("/parties/", methods=["GET"])
@login_required(role="ANY")
def parties_index():
    return render_template("parties/list.html", parties = Party.query.all(), form = PartySearch())

@app.route("/parties/", methods=["POST"])
@login_required(role="ANY")
def parties_search():
    form = PartySearch(request.form)
    form.search.data = form.search.data.strip()
    
    if not form.validate():
        return render_template("parties/list.html", parties = Party.query.all(), form = form)
    
    return render_template("parties/list.html", parties = Party.query.filter(Party.name.like("%"+form.search.data+"%")), form = form)

@app.route("/parties/new/", methods=["POST"])
@login_required(role="ANY")
def parties_create():
    form = PartyForm(request.form)

    if not form.validate():
        return render_template("parties/form.html", form = form)
    
    party = Party(form.name.data)
    party.business_id = form.business_id.data
    party.address_street = form.address_street.data
    party.address_postalcode = form.address_postalcode.data
    party.address_city = form.address_city.data
    party.bankrupt = False

    db.session().add(party)
    db.session().commit()
  
    return redirect(url_for("parties_view", party_id = party.id))

@app.route("/parties/new/", methods=["GET"])
@login_required(role="ANY")
def parties_new():
    form = PartyForm()
    return render_template("parties/form.html", form = form)

@app.route("/parties/<int:party_id>/", methods=["GET"])
@login_required(role="ANY")
def parties_view(party_id):
    party = Party.query.get_or_404(party_id)
    return render_template("parties/view.html", party = party, today = date.today())

@app.route("/parties/delete/<party_id>/", methods=["POST"])
@login_required(role="ANY")
def parties_delete(party_id):

    party = Party.query.get_or_404(party_id)

    db.session().delete(party)
    db.session().commit()

    return redirect(url_for("parties_index"))

@app.route("/parties/edit/<int:party_id>/", methods=["GET"])
@login_required(role="ANY")
def parties_edit_form(party_id):
    party = Party.query.get_or_404(party_id)
    form = PartyForm(obj=party)
    return render_template("parties/form.html", form = form, action = "edit", party_id = party_id)

@app.route("/parties/edit/<int:party_id>/", methods=["POST"])
@login_required(role="ANY")
def parties_edit(party_id):
    form = PartyForm(request.form)

    if not form.validate():
        return render_template("parties/form.html", form = form, action = "edit", party_id = party_id)

    editedParty = Party.query.get_or_404(party_id)
    editedParty.name = form.name.data
    editedParty.business_id = form.business_id.data
    editedParty.address_street = form.address_street.data
    editedParty.address_postalcode = form.address_postalcode.data
    editedParty.address_city = form.address_city.data

    db.session().add(editedParty)
    db.session().commit()
  
    return redirect(url_for('parties_view', party_id=party_id))

@app.route("/parties/<party_id>/setbankrupt/", methods=["POST"])
@login_required(role="ANY")
def parties_set_bankrupt(party_id):

    party = Party.query.get_or_404(party_id)
    party.bankrupt = True
    db.session().commit()

    Reminder.create_bankruptcy_reminders(party = party)

    return redirect(url_for('parties_view', party_id=party.id))

@app.route("/parties/<party_id>/unsetbankrupt/", methods=["POST"])
@login_required(role="ANY")
def parties_unset_bankrupt(party_id):

    party = Party.query.get_or_404(party_id)
    party.bankrupt = False
    db.session().commit()

    return redirect(url_for('parties_view', party_id=party.id))

@app.route("/parties/statistics/", methods=["GET"])
@login_required(role="ANY")
def parties_stats():
    return render_template("parties/stats.html",
        parties_count = Party.query.count(),
        bankrupt_count = Party.query.filter_by(bankrupt = True).count(),
        parties_with_most_contracts = Party.parties_with_most_contracts(),
        parties_with_most_valid_contracts = Party.parties_with_most_valid_contracts(),
        parties_with_no_contracts = Party.parties_with_no_contracts())