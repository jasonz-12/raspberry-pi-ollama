import torch
from TTS.api import TTS
import sounddevice as sd
import soundfile as sf
import numpy as np
import whisper
from ollama import chat
from ollama import ChatResponse
import ffmpeg
import pyaudio
import wave
import torch
import torchaudio
import webrtcvad