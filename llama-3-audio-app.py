from imports import *
from utils import *

# Initialize the conversation history
conversation_history = [
    {"role": "system", "content": "You are a helpful assistant, respond concisely and conversationally. You will be used in an audio app."}
]

while True:
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

    # Add the transcription to the conversation history
    conversation_history.append({"role": "user", "content": transcription})
    
    # Use the transcription as input for the llama3.2 model
    response: ChatResponse = chat(model='llama3.2:3b', messages=conversation_history)

    # or access fields directly from the response object
    response_text = response.message.content
    print("Response:", response_text)

    # Add the response to the conversation history
    conversation_history.append({'role': 'assistant', 'content': response_text})

    # Use the response to generate a TTS audio file
    try:
        # Initialize TTS
        tts = CoquiTTSWrapper()
        
        # Generate and play speech
        text = response.message.content
        wav, sr = tts.synthesize(text, "output.wav")
        tts.play_audio(wav, sr)
                
    except Exception as e:
        print(f"Error: {str(e)}")