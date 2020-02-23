# Rage chat
An awesome video chat app that doesn't really do video chat.
# App process
- Users join the video chat
- laptop webcam is enabled
- client snaps a screenshot every 3 seconds and sends it to the server
- server does image recognition on the photo and detects the emotion of the user
- user can also press record audio button to send an audio to their friend
- the audio is processed with a speech to text process
- the user gets the text result from their speech


## Setup
- install all the deps
	- just try and error, we didn't keep track of them all
- run `python app.py`
- go to the link that flask is served on
- your rage chat is ready
