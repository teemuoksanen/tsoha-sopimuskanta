from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required

from application.parties.models import Party
from application.parties.forms import PartyForm

@app.route("/parties/", methods=["GET"])
def parties_index():
    return render_template("parties/list.html", parties = Party.query.all())

@app.route("/parties/new/")
@login_required
def parties_form():
    return render_template("parties/form.html", form = PartyForm())

@app.route("/parties/<party_id>/setbankrupt/", methods=["POST"])
@login_required
def parties_set_bankrupt(party_id):

    party = Party.query.get(party_id)
    party.bankrupt = True
    db.session().commit()

    return redirect(url_for('parties_view', party_id=party.id))

@app.route("/parties/<party_id>/unsetbankrupt/", methods=["POST"])
@login_required
def parties_unset_bankrupt(party_id):

    party = Party.query.get(party_id)
    party.bankrupt = False
    db.session().commit()

    return redirect(url_for('parties_view', party_id=party.id))

@app.route("/parties/", methods=["POST"])
@login_required
def parties_create():
    form = PartyForm(request.form)

    if not form.validate():
        return render_template("parties/form.html", form = form)
    
    party = Party(form.name.data)
    party.business_id = form.businessid.data
    party.address_street = form.address_street.data
    party.address_postalcode = form.address_postalcode.data
    party.address_city = form.address_city.data
    party.bankrupt = form.bankrupt.data

    db.session().add(party)
    db.session().commit()
  
    return redirect(url_for("parties_index"))

@app.route("/parties/<int:party_id>/", methods=["GET"])
@login_required
def parties_view(party_id):
    party = Party.query.get(party_id)
    return render_template("parties/view.html", party = party)