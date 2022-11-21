from flask import Blueprint, flash, redirect, render_template, request, session, url_for, current_app
from flask_auth.db.db import db
from flask_auth.db.user import User
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash
import jwt

from .utils import check_registration_form, generate_token

auth = Blueprint("auth", __name__, template_folder="templates")


@auth.route("/")
def index():
    return render_template("login.html")


@auth.route("/reg", methods=["POST"])
def registration():
    form = request.form
    username = form["username"]
    password = form["pass"]
    confirm_password = form["confirm_pass"]

    this_url = url_for(".index", _anchor="register")

    validate = check_registration_form(username, password, confirm_password)
    if validate:
        flash(validate, "error")
        return redirect(this_url)

    password_hash = generate_password_hash(password)

    try:
        user = User(username=username, password=password_hash)

        db.session.add(user)
        db.session.commit()
    except IntegrityError as e:
        flash("Username exists", "error")
        return redirect(this_url)

    session["session"] = generate_token(username=user.username, id=user.id)
    flash("Successfull registration", "info")
    return redirect("/")


@auth.route("/login", methods=["POST"])
def login():

    return "ok"


@auth.route("/logout")
def logout():
    session.pop("session")
    
    return redirect("/")