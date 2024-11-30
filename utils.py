from imports import *

class CoquiTTSWrapper:
    def __init__(self, model_name="tts_models/en/ljspeech/vits", device="cpu"):
        """Initialize TTS with specified model"""
        try:
            self.device = "cuda" if torch.cuda.is_available() and device == "cuda" else "cpu"
            self.tts = TTS(model_name=model_name, progress_bar=True).to(self.device)
        except Exception as e:
            raise Exception(f"Failed to initialize TTS: {str(e)}")
        
    def list_models(self):
        """List available models"""
        return TTS().list_models()
    
    def synthesize(self, text, output_path=None, sample_rate=22050):
        """Generate speech from text"""
        try:
            wav = self.tts.tts(text=text)
            
            if output_path:
                sf.write(output_path, wav, sample_rate)
            
            return wav, sample_rate
            
        except Exception as e:
            raise Exception(f"Speech synthesis failed: {str(e)}")
    
    def play_audio(self, wav, sample_rate=22050):
        """Play audio using sounddevice"""
        try:
            sd.play(wav, sample_rate)
            sd.wait()
        except Exception as e:
            raise Exception(f"Audio playback failed: {str(e)}")

def record_audio(output_filename, sample_rate=16000, frame_length_ms=30):
    audio_format = pyaudio.paInt16
    channels = 1
    chunk_size = int(sample_rate * frame_length_ms / 1000)
    vad = webrtcvad.Vad()
    vad.set_mode(1)  # 0: Normal, 1: Low Bitrate, 2: Aggressive, 3: Very Aggressive

    audio = pyaudio.PyAudio()

    # Start recording
    stream = audio.open(format=audio_format, channels=channels,
                        rate=sample_rate, input=True,
                        frames_per_buffer=chunk_size)
    print("Recording...")
    frames = []
    silence_threshold = 30  # Number of silent chunks before stopping
    silence_count = 0

    while True:
        data = stream.read(chunk_size)
        frames.append(data)

        # Convert data to numpy array for VAD
        audio_data = np.frombuffer(data, dtype=np.int16)
        is_speech = vad.is_speech(audio_data.tobytes(), sample_rate)

        if not is_speech:
            silence_count += 1
        else:
            silence_count = 0

        if silence_count > silence_threshold:
            break

    print("Finished recording.")
    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the recorded data as a WAV file
    with wave.open(output_filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(audio_format))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))
    print(f"Audio data written to {output_filename}")