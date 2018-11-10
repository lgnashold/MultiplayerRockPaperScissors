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

        game_result = db.execute('SELECT id,name1,name2 FROM game WHERE joincode = ?', (join_code,)).fetchone()

        print(game_result)

        if game_result is None:
            #create new game
            db.execute(
                'INSERT INTO game (joincode,name1) VALUES (?,?)',(join_code,nickname)
            )
            db.commit()

        else:
            #join exsisting game
            pass

    return render_template("index.html")
