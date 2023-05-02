import whisper
import torch

print("Current device:", torch.cuda.current_device())
print("Device name:", torch.cuda.get_device_name(torch.cuda.current_device()))

model = whisper.load_model("small")
result = model.transcribe("recorded_audio.mp3")
print(result["text"])