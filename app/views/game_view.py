from flask import Blueprint, render_template, request
from ..controllers.game import generate_game

bp = Blueprint('game',__name__,'/play')

@bp.route("/")
def play():
    #TODO: Call generate_game() to create images and return them in a json format 
    meal_choice = request.args.get('data')
    

    return render_template('game.main_game.html')
