import os
from flask import render_template, current_app

from .soundboard import Soundboard


def init_app(app, socketio):
    global soundboard_instance
    soundboard_instance = Soundboard(socketio)

    @app.route("/dm")
    def dm_page():
        sounds = soundboard_instance.get_sounds()

        return render_template("dm.html", sounds=sounds)
    
    @app.route("/player")
    def player_page():
        return render_template("player.html")