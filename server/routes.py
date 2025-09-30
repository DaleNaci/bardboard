from flask import render_template


def init_app(app):
    @app.route("/dm")
    def dm_page():
        return render_template("dm.html")
    
    @app.route("/player")
    def player_page():
        return render_template("player.html")