import pyttsx3

def respond_with_audio(text):
    print(text)  # Display the text answer on screen

    # Initialize TTS engine
    engine = pyttsx3.init()

    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)

    # Speak only "Hello"
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    answer = "Hello! This is a text answer with audio feedback on your Raspberry Pi."
    respond_with_audio(answer)
