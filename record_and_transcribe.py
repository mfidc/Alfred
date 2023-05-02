import sounddevice as sd
import soundfile as sf
from pydub import AudioSegment
import io
import sys
import numpy as np
import whisper
import torch

model = whisper.load_model("small")

def transcribe_audio(audio_file):
    result = model.transcribe(audio_file)
    return result["text"]

def record_audio(duration, filename, samplerate=16000):
    print("Recording started. Speak into your microphone.")
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='float64')
    sd.wait()
    sf.write(filename, audio, samplerate)
    print(f"Recording saved as {filename}")

def main():
    print("Current device:", torch.cuda.current_device())
    print("Device name:", torch.cuda.get_device_name(torch.cuda.current_device()))

    duration = 30  # Duration of recording in seconds
    
    wav_filename = "recorded_audio.wav"
    mp3_filename = "recorded_audio.mp3"

    record_audio(duration, wav_filename)

    sound = AudioSegment.from_wav(wav_filename)
    sound.export(mp3_filename, format="mp3")

    with open(mp3_filename, "rb") as f:
        result = model.transcribe("recorded_audio.mp3")
        print(result["text"])


if __name__ == "__main__":
    main()
 