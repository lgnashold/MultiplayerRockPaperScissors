from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from . import socketio
from rps.db import get_db
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
    nickname = session["nickname"]
    join_code = session["join_code"]
    db = get_db()

    # Fetches game row
    result = db.execute("SELECT name1,move1,name2,move2 FROM game WHERE joincode = ?", (join_code,)).fetchone()
    colname = None

    if(result["name1"] == nickname):
        if(result["move1"] == None):
            colname = "move1"
    elif(result["name2"] == nickname):
        if(result["name2"] == None):
            colname ="move2"

    if(colname != None):
        db.execute("UPDATE game SET "+colname+" = :choice WHERE joincode = :jc", {"choice": choice["data"], "jc":join_code})
        db.commit()
