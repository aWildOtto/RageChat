import speech_recognition as sr
import pyttsx3
import wave
from gtts import gTTS
import os
import io
import base64

def audiototext(audioin):

    """
    nchannels = 1
    sampwidth = 1
    framerate = 8000
    nframes = 1

    name = 'output.wav'
    audio = wave.open(name, 'wb')
    audio.setnchannels(nchannels)
    audio.setsampwidth(sampwidth)
    audio.setframerate(framerate)
    audio.setnframes(nframes)

    blob = open(audioin).read()  # such as `blob.read()`
    audio.writeframes(blob)
    """


    print()
    decoded = base64.b64decode(audioin[22:])
    decoded = io.BytesIO(decoded)
    print("DECODEDE0")
    print(decoded)


    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.AudioFile(decoded) as source:
        r.adjust_for_ambient_noise(source)

        print("start listening")
        audio2 = r.record(source)
        print("Listening completed!")

    try:
        result = r.recognize_google(audio2)
        #print("[You said]: " + r.recognize_google(audio))
        print(str(result))

        """
        speech = gTTS(text = str(result), lang = 'en', slow = False)
        speech.save("text.wav")
        

        engine = pyttsx3.init()
        print("1")
        engine.say(result)
        print("2")
        engine.runAndWait()
        """

    except sr.UnknownValueError:
        print("Ooops! Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return str(result)