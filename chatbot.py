import speech_recognition as sr
import requests
import json
import time
from gtts import gTTS
import pygame
import io

def transcribe_audio(timeout=5):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Testing AI voice recognition...")
        try:
            audio = recognizer.listen(source, timeout=timeout)
            text = recognizer.recognize_google(audio, language="id-ID")
            print("User: " + text)
            return text
        except sr.WaitTimeoutError:
            print("Waktu habis. Tidak ada suara yang terdeteksi.")
            return None
        except sr.UnknownValueError:
            print("Maaf, saya tidak bisa mengenali apa yang Anda katakan.")
            return None
        except sr.RequestError as e:
            print("Tidak bisa meminta hasil dari layanan Google Speech Recognition; {0}".format(e))
            return None

def ask_gpt(prompt):
    url = "https://nexra.aryahcr.cc/api/chat/gpt"

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "messages": [
            {
                "role": "assistant",
                "content": "nama kamu sekarang adalah vbot"
            }
        ],
        "prompt": prompt,
        "model": "GPT-4",
        "markdown": False
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            response_json = response.json()
            response_text = response_json.get("gpt", "Tidak Menemukan Jawaban dari REST API")
            print("AI: " + response_text)
            return response_text
        else:
            print(f"Error: {response.status_code}")
            return None
    except Exception as e:
        print(e)
        return None

def text_to_speech(text):
    # Generate speech with gTTS
    tts = gTTS(text=text, lang='en')
    
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

if __name__ == "__main__":
    try:
        while True:
            # Transkripsi suara
            prompt_text = transcribe_audio()
            if prompt_text:
                # Mengirim prompt ke AI
                ai_response = ask_gpt(prompt_text)
                if ai_response:
                    # Mengubah respons AI menjadi suara
                    text_to_speech(ai_response)
            # Memberikan jeda sebelum menerima input berikutnya
            time.sleep(2)
    except KeyboardInterrupt:
        print("Program dihentikan oleh pengguna.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    finally:
        # Tambahkan kode cleanup di sini jika diperlukan
        print("Membersihkan sumber daya...")
