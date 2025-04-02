import pyttsx3

# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# for voice in voices:
#    print(voice.id)

import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 125)  # Slower speech


# List all available voices
voices = engine.getProperty('voices')
for i, voice in enumerate(voices):
    print(f"Voice {i}:")
    print(f" - ID: {voice.id}")
    print(f" - Name: {voice.name}")
    print(f" - Gender: {voice.gender}")
    print(f" - Language: {voice.languages}\n")

engine.stop()
