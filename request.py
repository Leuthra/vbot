import requests
import json

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
    "prompt": "siapa nama kamu?",
    "model": "GPT-4",
    "markdown": False
}

try:
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        response_json = response.json()
        print(response_json.get("gpt", "Tidak Menemukan Jawaban dari REST API"))
    else:
        print(f"Error: {response.status_code}")
except Exception as e:
    print(e)
'''
Namaku saat ini adalah vbot. Apakah ada yang bisa saya bantu?
'''
