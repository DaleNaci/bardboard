from flask import Flask
from flask_socketio import SocketIO
from server import routes, sockets


app = Flask(__name__)
socketio = SocketIO(app)

routes.init_app(app)
sockets.init_socket(socketio)


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)