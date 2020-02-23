import speech_recognition as sr
import pyttsx3
import wave

def audiototext(audioin):
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

    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.AudioFile(audio) as source:
        r.adjust_for_ambient_noise(source)

        print("start listening")
        audio2 = r.record(source)
        print("Listening completed!")

    try:
        result = r.recognize_google(audio2)
        #print("[You said]: " + r.recognize_google(audio))
        print(str(result))

        engine = pyttsx3.init()
        print("1")
        engine.say(result)
        print("2")
        engine.runAndWait()

    except sr.UnknownValueError:
        print("Ooops! Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

    return str(result)