from flask import render_template


def init_app(app):
    @app.route("/dm")
    def dm_page():
        sounds = ["brook.wav", "flask.wav"]
        return render_template("dm.html", sounds=sounds)
    
    @app.route("/player")
    def player_page():
        return render_template("player.html")