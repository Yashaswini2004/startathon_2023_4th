import speech_recognition as sr
AUDIO_FILE=('pythonnptel.wav')
r=sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio=r.record(source)
try:
    print("audio file contains",r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google speech recognition could not understand the audio")
except sr.RequestError:
    print("Couldnot able to get the result...")