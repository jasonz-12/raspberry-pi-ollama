import whisper

# Load the model
model = whisper.load_model("tiny")  # Options: tiny, base, small, medium, large

# Transcribe an audio file
result = model.transcribe("./audio/speech.mp3")  # Replace with your audio file path

# Print the result
print("Transcription:", result['text'])