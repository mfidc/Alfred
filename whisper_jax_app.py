from whisper_jax import FlaxWhisperPipline

# instantiate pipeline
pipeline = FlaxWhisperPipline("openai/whisper-small")

# JIT compile the forward call - slow, but we only do once
text = pipeline("recorded_audio.mp3")

# used cached function thereafter - super fast!!
text = pipeline("recorded_audio.mp3")