from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('matchmaking', __name__)

@bp.route("/", methods = ('GET','POST'))
def index():
    return render_template("index.html")

@bp.route("/join", methods = ('GET','POST'))
def join():
    return render_template("join.html")
