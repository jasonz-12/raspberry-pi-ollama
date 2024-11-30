from imports import *
from utils import *

def main():
    # Install required packages if not already installed:
    # pip install TTS torch sounddevice soundfile numpy
    
    try:
        # Initialize TTS
        tts = CoquiTTSWrapper()
        
        # Generate and play speech
        text = "Hope you're doing great in this fine morning!"
        wav, sr = tts.synthesize(text, "output.wav")
        tts.play_audio(wav, sr)
        
        # List available models
        print("\nAvailable models:")
        for model in tts.list_models():
            if "en" in model:  # Filter for English models
                print(f"- {model}")
                
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()