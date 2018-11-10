from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from rps.db import get_db

bp = Blueprint('matchmaking', __name__)

@bp.route("/", methods = ('GET','POST'))
def index():
    if request.method == "POST":
        nickname = request.form['nickname']
        join_code = request.form['join_code']

        db = get_db()

        game_result = db.execute('SELECT name1,name2,joincode FROM game WHERE joincode = ?', (join_code,)).fetchone()

        if game_result is None:
            #create new game
            db.execute(
                'INSERT INTO game (joincode,name1) VALUES (?,?)',(join_code,nickname)
            )
            db.commit()
            session["join_code"] = join_code
            session["user"] = nickname

            print(url_for('game.run_game'))
            return redirect(url_for('game.run_game'))

        else:
            #join exsisting game
            if game_result["name2"] != None:
                print("SORRY PAL. GAME IS FULL");
            else:
                db.execute(
                    'UPDATE game SET name2 = (?) WHERE joincode = (?)',(nickname,join_code)
                )
                db.commit()
                session["join_code"] = game_result["joincode"]
                session["user"] = nickname
                return redirect(url_for('game.run_game'))


    return render_template("index.html")
