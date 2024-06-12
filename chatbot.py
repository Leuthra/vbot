import speech_recognition as sr
import requests
import json
import pyttsx3
import time

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
                "content": "Hello! How are you today?"
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
            response_text = response_json.get("gpt", "Error: no response text found")
            print("AI: " + response_text)
            return response_text
        else:
            print(f"Error: {response.status_code}")
            return None
    except Exception as e:
        print(e)
        return None

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

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
