from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, leave_room
import emotions

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)

alldata = {}
@app.route('/')
def sessions():
    return render_template('session.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('message')
def handle_message_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    socketio.send({	"type": "Connection:", "content": username + ' has entered the room ' + room}, room=room)

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    socketio.send(username + ' has left the room.', room=room)

@socketio.on('photo')
def handle_photo_event(data, methods=['GET', 'POST']):
    print("received photo")
    # print(photo)
    # print(data)
    emotion = emotions.tell_emotion(data['photo'])
		# photo is based64 blob, decode and do emotion detection
		# do emotion detection
    socketio.emit('photo result', {"username": data['username'], "emotion": emotion})

@socketio.on('audio')
def handle_audio_event(data, methods=['GET', 'POST']):
    print("received audio ", data['username'])
    # TODO: do audio processing here
    newAudio = data["audio"] # this should be computer generated voice
    text = "David sucks ass" # this should be NLP text
    socketio.emit('audio result', {"username": data['username'], "audio": newAudio, "text": text })

if __name__ == '__main__':
    socketio.run(app, debug=True)
