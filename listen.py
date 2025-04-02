import os
import ollama
import speech_recognition as sr

# source my_venv/bin/activate


# Initialize the recognizer
recognizer = sr.Recognizer()

def listen_and_run():
    with sr.Microphone() as source:
        print("Listening for command...")
        try:
            audio = recognizer.listen(source, timeout=30)  # listen for 5 seconds
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")

            if "drive" in command:
                print("Running the script...1")
                os.system('espeak-ng -v en-us -s 120 "Sure I can drive where you ask me to."')
                # os.system("python3 /path/to/your_script.py")
            elif "go to sleep" in command:
                print("Running the script...2")
                os.system('espeak-ng -v en-us -s 120 "I can not sleep but I can charge my battery to use it later."')
            elif "stop" in command:
                print("Running the script...3")
                os.system('espeak-ng -v en-us -s 120 "Im breaking my mission and stopping my heart."')
            else:
                # print("Command not recognized.")
                # Send the question to Ollama and get the response
                # response = ollama.chat(command)
                response = ollama.chat(
                    model='llama3.2',
                    messages=[
                        {
                            'role': 'user',
                            'content': f"{command}"
                            }
                        ]
                    )
                print(f'Command: {command}')
                print(f"OLLAMA Response: {response['message']['content']}")  # Example: "STOP"
                os.system(f'espeak-ng -s 120 "{response["message"]["content"]}"')
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand the command.")
        except sr.RequestError:
            print("Error with the speech recognition service.")
        except sr.WaitTimeoutError:
            print("No command heard. Try again.")
        
if __name__ == "__main__":
    listen_and_run()
