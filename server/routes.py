import os
from flask import render_template, current_app


def init_app(app):
    @app.route("/dm")
    def dm_page():
        folder = os.path.join(current_app.root_path, "static", "sounds")
        sounds = [f for f in os.listdir(folder)]

        return render_template("dm.html", sounds=sounds)
    
    @app.route("/player")
    def player_page():
        return render_template("player.html")