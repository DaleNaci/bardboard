from flask_socketio import SocketIO, emit, disconnect


state = {"currentTrack": None, "startTime": None, "isPlaying": None}

def init_socket(socketio: SocketIO):
    @socketio.on("connect")
    def handle_connect():
        emit("state_update", state)
    
    @socketio.on("update_state")
    def handle_update(data):
        global state
        state = data

        emit("state_update", state, broadcast=True)
    
    @socketio.on("disconnect")
    def handle_disconnect():
        print("Client disconnected.")