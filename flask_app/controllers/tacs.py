from flask_app import app
from flask import flash

from flask_app.models.tac import TicTacToe

from flask import render_template, request, redirect, session, make_response

from easyAI import TwoPlayerGame, Human_Player, AI_Player, Negamax

ai_algo = Negamax(6)

@app.route("/tac-toe-tic", methods=["GET", "POST"])
def play_game():
    ttt = TicTacToe([Human_Player(), AI_Player(ai_algo)])
    game_cookie = request.cookies.get("game_board")
    if game_cookie:
        ttt.board = [int(x) for x in game_cookie.split(",")]
    if "choice" in request.form:
        ttt.play_move(request.form["choice"])
        if not ttt.is_over():
            ai_move = ttt.get_move()
            ttt.play_move(ai_move)
    if "reset" in request.form:
        ttt.board = [0 for i in range(9)]
    if ttt.is_over():
        msg = ttt.winner()
    else:
        msg = "play move"
    resp = make_response(render_template("tac_toe_tic.html", ttt=ttt, msg=msg))
    c = ",".join(map(str, ttt.board))
    resp.set_cookie("game_board", c)
    return resp