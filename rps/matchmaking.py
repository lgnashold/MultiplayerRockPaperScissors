from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from rps.db import get_db

bp = Blueprint('matchmaking', __name__)

@bp.route("/", methods = ('GET','POST'))
def index():
    if request.method == "POST":
        db = get_db()
        db.execute(
            'INSERT INTO game (move1,move2) VALUES (?,?)',(0,0)
        )
        db.commit()

    return render_template("index.html")

@bp.route("/join", methods = ('GET','POST'))
def join():
    return render_template("join.html")
