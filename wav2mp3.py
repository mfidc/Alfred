import pydub

sound = pydub.AudioSegment.from_wav("recorded_audio.wav")
sound.export("recorded_audio.mp3", format="mp3")