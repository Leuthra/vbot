import speech_recognition as sr
import os
import webbrowser
import requests
import json
import datetime
from gtts import gTTS
import pygame
import io

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
                "content": "nama kamu sekarang adalah vbot"
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
            response_text = response_json.get("gpt", "Tidak Menemukan Jawaban dari REST API")
            say(response_text)
            chatStr += f"{response_text}\n"
            return response_text
        else:
            print(f"Error: {response.status_code}")
            return "Tidak dapat menangani error dari REST API"
    except Exception as e:
        print(e)
        return "Tidak dapat menangani error dari REST API"

def say(text):
    # Generate speech with gTTS
    tts = gTTS(text=text, lang='id')
    
    # Save the speech to a BytesIO object
    mp3_fp = io.BytesIO()
    tts.write_to_fp(mp3_fp)
    mp3_fp.seek(0)
    
    # Initialize pygame mixer
    pygame.mixer.init()
    pygame.mixer.music.load(mp3_fp, 'mp3')
    pygame.mixer.music.play()
    
    # Wait for the speech to finish playing
    while pygame.mixer.music.get_busy():
        continue

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Silakan Berbicara...")
        audio = r.listen(source)
        try:
            print("Mendengarkan...")
            query = r.recognize_google(audio, language="id-ID")
            print(f"User: {query}")
            return query
        except sr.UnknownValueError:
            print("Tidak dapat mengenali suara")
            return "Tidak dapat mengenali suara"
        except sr.RequestError as e:
            print(f"Tidak dapat menerima Request; {e}")
            return "Maaf, koneksi error"
        except Exception as e:
            print(e)
            return "Kerusakan pada VBOT, tidak dapat menerima input"

if __name__ == '__main__':
    print('Starting Bot...')
    say("Halo, saya VBOT. Ada yang bisa saya bantu?")
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
                say("Opening Spotify")
                os.startfile(r"C:\Users\user\Desktop\Spotify.lnk")

            elif "the time" in query:
                hour = datetime.datetime.now().strftime("%H")
                min = datetime.datetime.now().strftime("%M")
                say(f"Sekarang jam {hour} dan {min} menit")

            elif "open facetime" in query:
                os.system("start Facetime")

            elif "open pass" in query:
                os.system("start Passky")

            elif "using artificial intelligence" in query:
                chat(query)

            elif "bot quit" in query:
                say("Terima kasih, sampai jumpa lagi!")
                break

            elif "reset chat" in query:
                chatStr = ""

            else:
                print("Chatting...")
                chat(query)
        except KeyboardInterrupt:
            print("Exiting Bot...")
            break
