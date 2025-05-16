from flask import Blueprint, render_template
from flask_login import login_required

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def welcome():
    return render_template("base.html")  # make sure this file exists in templates/

@main_bp.route("/home")
@login_required
def home():
    return render_template("home.html")
