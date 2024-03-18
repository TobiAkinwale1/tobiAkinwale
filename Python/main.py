import speech_recognition as sr
from datetime import datetime

# Initialize the recognizer
r = sr.Recognizer()

# Record Audio
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# Try recognizing the speech
try:
    text = r.recognize_google(audio)
    print("You said: " + text)

    # Save the text in a new file
    filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".txt"
    with open(filename, "w") as file:
        file.write(text)
    print(f"Text saved in file {filename}")

except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
