from application import app, db
from flask import redirect, render_template, request, url_for
from application.parties.models import Party

@app.route("/parties", methods=["GET"])
def parties_index():
    return render_template("parties/list.html", parties = Party.query.all())

@app.route("/parties/new/")
def parties_form():
    return render_template("parties/new.html")

@app.route("/parties/bankrupt/<party_id>/", methods=["POST"])
def parties_set_bankrupt(party_id):

    party = Party.query.get(party_id)
    party.bankrupt = True
    db.session().commit()

    return redirect(url_for("parties_index"))

@app.route("/parties/", methods=["POST"])
def parties_create():
    party = Party(request.form.get("name"))

    db.session().add(party)
    db.session().commit()
  
    return redirect(url_for("parties_index"))
