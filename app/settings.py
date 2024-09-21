from flask import Blueprint
from flask import request, url_for, redirect
from flask import render_template
bp = Blueprint('settings',__name__,url_prefix="/settings")

@bp.route("/",methods=['GET','POST'])
def settings():
    if request.method == "POST":
        choice = request.form['options']
        
        #TODO set choice as environment variable to be pulled into request to ai
        return redirect(url_for("game.play_game",data=choice))
    else:
        return render_template('settings/settings.html')