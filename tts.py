from TTS.api import TTS

# Initialize the TTS model (you can use different pre-trained models)
# For example, this loads a model trained on English (LJSpeech dataset)
tts = TTS("tts_models/en/ljspeech/tacotron2-DDC")

# Text to be converted into speech
text = "Hello, this is your Raspberry Pi speaking."

# Convert text to speech and save it as a .wav file
tts.tts_to_file(text=text, file_path="output.wav")

# Optionally, you can use pyaudio to play the audio
import os
os.system("aplay output.wav")
