from application import app, db
from flask import redirect, render_template, request, url_for
from application.contracts.models import Contract

@app.route("/contracts", methods=["GET"])
def contracts_index():
    return render_template("contracts/list.html", contracts = Contract.query.all())

@app.route("/contracts/new/")
def contracts_form():
    return render_template("contracts/new.html")

@app.route("/contracts/", methods=["POST"])
def contracts_create():
    contract = Contract(request.form.get("name"))

    db.session().add(contract)
    db.session().commit()
  
    return redirect(url_for("contracts_index"))