# Voice Recognition and AI Chat Bot

This repository contains two Python scripts that implement a voice recognition system integrated with a GPT-4 based AI chat bot. These scripts are `chatbot.py` and `main.py`.

## Features

- Voice recognition using Google Speech Recognition.
- Interaction with a GPT-4 AI model via API for conversational responses.
- Text-to-speech conversion to provide audio responses.
- Ability to open web pages and perform specific commands based on voice input.

## Requirements

To run these scripts, you need the following Python libraries:
- `speech_recognition`
- `requests`
- `json`
- `pyttsx3`
- `datetime`

You can install these libraries using `pip`:
```bash
pip install speechrecognition requests pyttsx3
```

## Usage

### transcribe.py

This script continuously listens for audio input, transcribes it, sends it to the GPT-4 AI for a response, and then converts the response back to speech.

#### How to run:
```bash
python chatbot.py
```

### Code Overview:

- `transcribe_audio(timeout=5)`: Listens to audio input and transcribes it.
- `ask_gpt(prompt)`: Sends the transcribed text to the GPT-4 AI and retrieves a response.
- `text_to_speech(text)`: Converts the AI's text response to speech.

### main.py

This script performs a similar function to `chatbot.py` but includes additional commands for opening web pages and specific applications.

#### How to run:
```bash
python main.py
```

### Code Overview:

- `chat(query)`: Sends a user query to the GPT-4 AI and retrieves a response.
- `say(text)`: Converts text to speech.
- `takeCommand()`: Listens to audio input and transcribes it.
- Includes command handling for opening YouTube, Wikipedia, Google, Spotify, and providing the current time.

## Customization

- You can modify the voice commands in `main.py` by adding new `elif` conditions in the main loop.
- The `ask_gpt` function in both scripts can be updated to point to a different API endpoint if needed.

## Notes

- Ensure your microphone is properly configured and accessible by your system.
- The GPT-4 API URL and the API itself used in these scripts are hypothetical. Replace `https://nexra.aryahcr.cc/api/chat/gpt` with your actual API endpoint.
- Be mindful of API usage limits and costs associated with using GPT-4.

## License

This project is licensed under the Apache License. See the `LICENSE` file for details.
