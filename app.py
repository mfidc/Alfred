from flask import Flask, render_template, request, jsonify
from but import main
import threading
import numpy as np
from openai_utils import initialize_openai, read_api_key
import whisper
import torch
from pydub import AudioSegment
import io

app = Flask(__name__)

api_key = read_api_key("openai_api_key.txt")
initialize_openai(api_key)

print("Current device:", torch.cuda.current_device())
print("Device name:", torch.cuda.get_device_name(torch.cuda.current_device()))

model = whisper.load_model("small")

messages = []
context = []
message_summarys = []


def transcribe_audio(audio_file):
    result = model.transcribe(audio_file)
    return result["text"]


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/send_message', methods=['POST'])
def send_message():
    if 'message' in request.get_json():
        message = request.get_json()['message']
    elif 'audio' in request.files:
        audio_file = request.files.get('audio')
        if audio_file.content_type == 'audio/webm':
            audio = AudioSegment.from_file(io.BytesIO(audio_file.read()), format='webm')
            audio.export("recorded_audio.mp3", format="mp3")
            with open("recorded_audio.mp3", "rb") as f:
                message = transcribe_audio(f)
        else:
            return jsonify({'error': 'Unsupported audio format'}), 400
    else:
        return jsonify({'error': 'No message or audio file provided'}), 400

    response = main(message, messages, message_summarys, context)
    return jsonify({'response': response})


if __name__ == '__main__':
    app.run(debug=True)
