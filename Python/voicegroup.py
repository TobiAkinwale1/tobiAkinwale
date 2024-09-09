import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

import speech_recognition as sr
from textblob import TextBlob


def classify_audio():
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Use the microphone as source for input.
    with sr.Microphone() as source:
        print("Please speak now...")
        audio_data = recognizer.listen(source)
        print("Recognizing...")

        # Convert speech to text
        try:
            text = recognizer.recognize_google(audio_data)
            print("You said: " + text)

            # Perform sentiment analysis
            analysis = TextBlob(text)
            polarity = analysis.sentiment.polarity

            # Classify based on polarity
            if polarity < 0:
                print("This sounds like a complaint.")
            else:
                print("This sounds like an inquiry.")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")


if __name__ == "__main__":
    classify_audio()
