from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('game', __name__, url_prefix='/game')

@bp.route("/game", methods = ('GET','POST'))
def run_game():
    print(session["join_code"])
    if session["join_code"] != None :
        render_template("game.html", join_code = join_code)
    else:
        redirect(url_for(index))
