# Rage chat
An awesome video chat app that doesn't really do video chat. This video chat app doesn't show the users the video feed but instead shows rage faces coorisponding to user's emotion detected. User can talk to the mic and the speech will be converted to text and displayed as subtitles under the rage face.

## App process
- Users join the video chat
- laptop webcam is enabled
- client snaps a screenshot every 3 seconds and sends it to the server
- server does image recognition on the photo and detects the emotion of the user
- Instead of seeing the users' video feed, we show them a picture of rage face coorisponding their emotions
- user can also press record audio button to send an audio to their friend
- the audio is processed with a speech to text process
- the user gets the text result from their speech

![angry face](https://github.com/aWildOtto/definitelyAvideoChat/blob/master/static/resized_angry.png)
![disgusted face](https://github.com/aWildOtto/definitelyAvideoChat/blob/master/static/resized_disgusted.png)
![fearful face](https://github.com/aWildOtto/definitelyAvideoChat/blob/master/static/resized_fearful.png)
![happy face](https://github.com/aWildOtto/definitelyAvideoChat/blob/master/static/resized_happy.png)
![neutral face](https://github.com/aWildOtto/definitelyAvideoChat/blob/master/static/resized_neutral.png)
![sad face](https://github.com/aWildOtto/definitelyAvideoChat/blob/master/static/resized_sad.png)
![surprised face](https://github.com/aWildOtto/definitelyAvideoChat/blob/master/static/resized_surprised.png)

## Setup
- install all the deps
	- just try and error, we didn't keep track of them all
- run `python app.py`
- go to the link that flask is served on
- your rage chat is ready

## Stack
- HTML
- JQuery
- Bootstrap
- Flask
- OpenCV
- Tensorflow
