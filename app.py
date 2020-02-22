from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

@app.route('/')
def sessions():
    return render_template('session.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('message')
def handle_message_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

@socketio.on('photo')
def handle_photo_event(photo, methods=['GET', 'POST']):
    print("received photo")
		# photo is based64 blob, decode and do emotion detection
		# do emotion detection
    socketio.emit('photo result', "angry")

if __name__ == '__main__':
    socketio.run(app, debug=True)