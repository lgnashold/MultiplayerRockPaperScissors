from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from . import socketio
from . import db.get_db
bp = Blueprint('game', __name__)

@bp.route("/game", methods = ('GET','POST'))
def run_game():
    print("this runs")
    if session["join_code"] != None :
        return render_template("game.html", join_code = session["join_code"], nickname = session["nickname"])
    else:
        return redirect(url_for(index))

@socketio.on("made_move")
def move_input(choice):
    print(choice)
    name = session["name"]
    game = session["join_code"]
    db = get_db() 
