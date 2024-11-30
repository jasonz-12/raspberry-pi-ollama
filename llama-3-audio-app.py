from imports import *
from utils import *
# Record audio from the microphone
audio_filename = "./audio/input.wav"
record_audio(audio_filename)

# Load the Whisper model
model = whisper.load_model("tiny")  # Options: tiny, base, small, medium, large

# Transcribe the recorded audio file
result = model.transcribe(audio_filename)

# Print the transcription result
transcription = result['text']
print("Transcription:", transcription)

# Use the transcription as input for the llama3.2 model
response: ChatResponse = chat(model='llama3.2:1b', messages=[
  {
    'role': 'user',
    'content': transcription,
  },
])

# or access fields directly from the response object
print(response.message.content)

# Use the response to generate a TTS audio file
try:
    # Initialize TTS
    tts = CoquiTTSWrapper()
    
    # Generate and play speech
    text = response.message.content
    wav, sr = tts.synthesize(text, "output.wav")
    tts.play_audio(wav, sr)
    
    # List available models
    print("\nAvailable models:")
    for model in tts.list_models():
        if "en" in model:  # Filter for English models
            print(f"- {model}")
            
except Exception as e:
    print(f"Error: {str(e)}")