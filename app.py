from flask import Flask
from flask_socketio import SocketIO
# from server import routes, sockets
from server.routes import init_app


app = Flask(__name__)
socketio = SocketIO(app)

init_app(app, socketio)

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5001, debug=True)