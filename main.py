import speech_recognition as sr
import os
import webbrowser
import requests
import json
import datetime
import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()
chatStr = ""

def chat(query):
    global chatStr
    print(chatStr)
    url = "https://nexra.aryahcr.cc/api/chat/gpt"
    headers = {
        "Content-Type": "application/json"
    }
    chatStr += f"User: {query}\nAssistant: "
    data = {
        "messages": [
            {
                "role": "assistant",
                "content": "Hello! How are you today?"
            }
        ],
        "prompt": query,
        "model": "GPT-4",
        "markdown": False
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            response_json = response.json()
            response_text = response_json.get("gpt", "Error in response")
            say(response_text)
            chatStr += f"{response_text}\n"
            return response_text
        else:
            print(f"Error: {response.status_code}")
            return "I'm sorry, I encountered an error."
    except Exception as e:
        print(e)
        return "I'm sorry, I encountered an error."

def say(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="id-ID")
            print(f"User said: {query}")
            return query
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return "Sorry, I did not understand that."
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return "Sorry, I am having trouble connecting."
        except Exception as e:
            print(e)
            return "Some Error Occurred. Sorry from Bot"

if __name__ == '__main__':
    print('Starting Bot...')
    say("Hello Sir! I am Bot. How can I help you?")
    while True:
        try:
            query = takeCommand().lower()

            if "open youtube" in query:
                say("Opening YouTube")
                webbrowser.open("https://www.youtube.com")

            elif "open wikipedia" in query:
                say("Opening Wikipedia")
                webbrowser.open("https://www.wikipedia.com")

            elif "open google" in query:
                say("Opening Google")
                webbrowser.open("https://www.google.com")

            elif "open spotify" in query:
                say("Opening Google")
                os.startfile(r"C:\Users\user\Desktop\Spotify.lnk")

            elif "the time" in query:
                hour = datetime.datetime.now().strftime("%H")
                min = datetime.datetime.now().strftime("%M")
                say(f"Sir, the time is {hour} hours and {min} minutes")

            elif "open facetime" in query:
                os.system("start Facetime")

            elif "open pass" in query:
                os.system("start Passky")

            elif "using artificial intelligence" in query:
                chat(query)

            elif "bot quit" in query:
                say("Goodbye Sir!")
                break

            elif "reset chat" in query:
                chatStr = ""

            else:
                print("Chatting...")
                chat(query)
        except KeyboardInterrupt:
            print("Exiting Bot...")
            break
