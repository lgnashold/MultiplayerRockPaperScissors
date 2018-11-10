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
        evaluate_game(join_code)
    
def evaluate_game(join_code):
    #Fetch Game
    db = get_db()
    result = db.execute("SELECT name1, move1, name2, move2 FROM game WHERE joincode = ?",(join_code,)).fetchone()
    
    move1 = result["move1"]
    move2 = result["move2"]
    
    
    #If both moves are full, emit messages
    if(move1 != None and move2 != None):
        msg = result["name1"] + " played " + move1 + ", " + result["name2"] + " played " + move2 +". "
        if(move1 == move2):
            msg += "It's a tie!"
        elif( (move1 == "paper" and move2 == "rock") or (move1 == "scissors" and move2 == "paper") or (move1 == "rock" and move2 == "scissors")):
            msg += results[name1] + " won!!"
        else:
            msg += results[name2] + " won!!"
        db.execute("UPDATE game set move1 = NULL, move2 = NULL WHERE joincode = (?)", (join_code,))
        db.commit()

        emit("response", {"data":msg})
            

