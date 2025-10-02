import os
from flask import current_app
from flask_socketio import SocketIO


class Soundboard:
    def __init__(self, socketio: SocketIO):
        self.socketio = socketio
        self.state = {"currentTrack": None, "isPlaying": False}
        self.history = []
        self.register_events()


    def get_sounds(self):
        sounds_folder = os.path.join(current_app.root_path, "static", "sounds")
        
        return [f for f in os.listdir(sounds_folder)]


    def register_events(self):
        @self.socketio.on("connect")
        def handle_connect():
            self.socketio.emit("state_update", self.state)
        

        @self.socketio.on("play_sound")
        def handle_play_sound(data):
            self.state["currentTrack"] = data["filename"]
            self.state["isPlaying"] = True
            self.history.append(data["filename"])
            self.socketio.emit("play_sound", data, include_self=True)