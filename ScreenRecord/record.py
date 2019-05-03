import wave
import pyaudio
#from pyaudio import PyAudio,paInt16
from PIL import ImageGrab
import numpy as np
import cv2
from moviepy.editor import *
from moviepy.audio.fx import all
import time
import pyautogui
import sys
import datetime

#get time laber to ser file name
now_time = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

#set video file name and video freame number 
VIDEO_OUTPUT_FILENAME="recoed_video"+now_time+".mp4"
VIDEO_FREAME=24

#set audio rate,chunk and audio file name
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
WAVE_OUTPUT_FILENAME ="recoed_aduio"+now_time+".wav"


p = pyaudio.PyAudio()
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
#set audio flag ==true
audio_record_flag = True

audio_tmp="b'\xfd\xff\xfe\xff\x01\x00\x00\x00\x01\x00\x00\x00\x04\x00\x04\x00\x03\x00\x04\x00\x01\x00\x01\x00\x02\x00\x02\x00\t\x00\x08\x00\x03\x00\x03\x00\x02\x00\x01\x00\xfd\xff\xfb\xff\x02\x00\x03\x00\x03\x00\x04\x00\xfe\xff\xff\xff\x03\x00\x02\x00\xfe\xff\xfe\xff\x00\x00\xff\xff\x00\x00\x02\x00\x06\x00\x07\x00\x06\x00\x05\x00\x01\x00\x01\x00\x03\x00\x03\x00\x01\x00\x02\x00\x05\x00\x04\x00\x06\x00\x07\x00\x07\x00\x07\x00\x06\x00\x07\x00\x08\x00\t\x00\x02\x00\x02\x00\xff\xff\xff\xff\xfe\xff\x00\x00\x01\x00\x01\x00\x00\x00\xff\xff\xff\xff\x01\x00\xff\xff\xff\xff\xff\xff\xff\xff\xfd\xff\xfe\xff\x00\x00\xff\xff\x00\x00\xff\xff\xfe\xff\xff\xff\x01\x00\x00\x00\xf9\xff\xf9\xff\xfb\xff\xfc\xff\xfc\xff\xfc\xff\xfc\xff\xfd\xff\x00\x00\x01\x00\xff\xff\x00\x00\xfa\xff\xfc\xff\xfa\xff\xfb\xff\xfd\xff\xfd\xff\xf7\xff\xf7\xff\xf7\xff\xf7\xff\xf8\xff\xf8\xff\xfb\xff\xfa\xff\xf8\xff\xf8\xff\xf7\xff\xf7\xff\xfb\xff\xfb\xff\xf7\xff\xf7\xff\xfa\xff\xfa\xff\xff\xff\xff\xff\xf9\xff\xfb\xff\xfd\xff\xfe\xff\xfb\xff\xfb\xff\xfd\xff\xfd\xff\x03\x00\x02\x00\xf6\xff\xf6\xff\xfd\xff\xfb\xff\xfb\xff\xfb\xff\xfb\xff\xfb\xff\x05\x00\x05\x00\x01\x00\x01\x00\xfd\xff\xfc\xff\xfb\xff\xfb\xff\xf8\xff\xf7\xff\xff\xff\xfe\xff\xfe\xff\xfd\xff\xfc\xff\xfd\xff\xfd\xff\xfc\xff\xfc\xff\xfc\xff\x02\x00\x01\x00\xfd\xff\xfd\xff\x02\x00\x02\x00\xff\xff\xff\xff\xf4\xff\xf3\xff\xff\xff\xff\xff\x01\x00\x00\x00\xfc\xff\xfb\xff\xf7\xff\xf6\xff\xfc\xff\xfc\xff\x02\x00\x02\x00\xfb\xff\xfb\xff\x00\x00\x00\x00\xff\xff\xff\xff\xfd\xff\xfe\xff\xf8\xff\xfa\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfb\xff\xfa\xff\xfd\xff\xfe\xff\xfd\xff\xfd\xff\x04\x00\x03\x00\x02\x00\x00\x00\xfb\xff\xfa\xff\xf9\xff\xf9\xff\xfe\xff\xfe\xff\xf5\xff\xf4\xff\xfc\xff\xfc\xff\x02\x00\x02\x00\xf8\xff\xf8\xff\x00\x00\x00\x00\x02\x00\x03\x00\x03\x00\x03\x00\x04\x00\x03\x00\x04\x00\x03\x00\x01\x00\x00\x00\xfd\xff\xff\xff\xfe\xff\xfe\xff\xfb\xff\xfc\xff\xff\xff\xff\xff\xfd\xff\xfd\xff\xfe\xff\xfd\xff\xfe\xff\xfd\xff\x01\x00\x01\x00\xff\xff\x00\x00\x01\x00\x01\x00\xfb\xff\xfa\xff\xf4\xff\xf3\xff\xfd\xff\xfc\xff\xfc\xff\xfd\xff\xf8\xff\xf8\xff\xf9\xff\xfa\xff\xf4\xff\xf4\xff\xf8\xff\xf9\xff\xff\xff\x00\x00\xfc\xff\xfc\xff\xfa\xff\xf9\xff\xfa\xff\xf8\xff\xfa\xff\xfb\xff\xff\xff\x00\x00\xf7\xff\xf8\xff\xf8\xff\xf8\xff\xff\xff\xfe\xff\xfb\xff\xfd\xff\x03\x00\x04\x00\xf7\xff\xf7\xff\xfd\xff\xfd\xff\xff\xff\xfe\xff\x00\x00\x00\x00\xff\xff\xff\xff\xfb\xff\xfb\xff\xfd\xff\xfe\xff\xf9\xff\xf9\xff\xfa\xff\xfb\xff\xfc\xff\xfc\xff\xf6\xff\xf5\xff\xfd\xff\xfb\xff\x02\x00\x02\x00\xfa\xff\xf9\xff\x02\x00\x03\x00\xfe\xff\xfd\xff\xf4\xff\xf4\xff\xfe\xff\x00\x00\xfc\xff\xfb\xff\xf6\xff\xf8\xff\xf5\xff\xf4\xff\xfa\xff\xfa\xff\xfb\xff\xfc\xff\xfe\xff\xff\xff\x03\x00\x04\x00\xfc\xff\xfd\xff\xfc\xff\xfd\xff\xfa\xff\xfb\xff\xf9\xff\xf8\xff\xfd\xff\xfd\xff\xfa\xff\xfa\xff\x01\x00\x01\x00\xfe\xff\xfe\xff\xfe\xff\xfd\xff\x01\x00\x01\x00\xfb\xff\xfa\xff\x01\x00\x02\x00\xff\xff\x00\x00\xff\xff\xff\xff\x05\x00\x05\x00\x03\x00\x03\x00\x01\x00\x01\x00\xfe\xff\xfe\xff\x00\x00\x00\x00\x03\x00\x03\x00\x07\x00\x08\x00\xff\xff\xfe\xff\x04\x00\x04\x00\x04\x00\x04\x00\x00\x00\xff\xff\xfe\xff\xfd\xff\xfb\xff\xfb\xff\x08\x00\x08\x00\x00\x00\x00\x00\x03\x00\x03\x00\x00\x00\x00\x00\x02\x00\x02\x00\x03\x00\x03\x00\xfa\xff\xfb\xff\x02\x00\x02\x00\xf9\xff\xfa\xff\xfa\xff\xfa\xff\xff\xff\xff\xff\xfb\xff\xfb\xff\xfd\xff\xfd\xff\x00\x00\x00\x00\xfc\xff\xfc\xff\xf7\xff\xf6\xff\x03\x00\x02\x00\xfc\xff\xfb\xff\xf9\xff\xf8\xff\xfd\xff\xfb\xff\xfe\xff\xfd\xff\xfb\xff\xfb\xff\xfc\xff\xfb\xff\xfe\xff\xfd\xff\xfb\xff\xfb\xff\x03\x00\x02\x00\x02\x00\x01\x00\x00\x00\x00\x00\xfc\xff\xfb\xff\xfe\xff\xfc\xff\xfa\xff\xf9\xff\xff\xff\x00\x00\xfb\xff\xfc\xff\xfc\xff\xfa\xff\xfe\xff\xff\xff\xfb\xff\xfc\xff\x00\x00\xff\xff\x07\x00\x07\x00\x02\x00\x01\x00\x02\x00\x02\x00\x07\x00\x07\x00\x06\x00\x06\x00\x03\x00\x03\x00\xfd\xff\xfc\xff\x06\x00\x04\x00\xfd\xff\xfe\xff\xfe\xff\xfe\xff\x02\x00\x02\x00\x00\x00\x01\x00\xfe\xff\x00\x00\xfe\xff\xfd\xff\xfc\xff\xfc\xff\xfa\xff\xfc\xff\xf7\xff\xf8\xff\xfd\xff\xfd\xff\xfe\xff\xfd\xff\xfe\xff\xff\xff\x01\x00\x01\x00\xfc\xff\xfc\xff\xfd\xff\xfe\xff\xfd\xff\xfe\xff\x02\x00\x01\x00\x06\x00\x07\x00\xfa\xff\xfc\xff\xfe\xff\xfe\xff\xfe\xff\xfe\xff\xfd\xff\xfe\xff\xfa\xff\xf9\xff\xfc\xff\xfc\xff\x00\x00\x00\x00\xfe\xff\xfe\xff\x02\x00\x02\x00\xfd\xff\xfe\xff\x01\x00\x01\x00\x05\x00\x05\x00\x01\x00\x00\x00\xff\xff\xfe\xff\x06\x00\x06\x00\x04\x00\x04\x00\x02\x00\x03\x00\x02\x00\x03\x00\t\x00\x08\x00\x0b\x00\t\x00\x05\x00\x04\x00\x03\x00\x03\x00\x04\x00\x05\x00\n\x00\x0b\x00\x07\x00\x07\x00\x06\x00\x05\x00\x06\x00\x04\x00\x01\x00\x01\x00\x04\x00\x04\x00\x06\x00\x06\x00\x05\x00\x05\x00\x05\x00\x03\x00\x07\x00\x07\x00\x03\x00\x02\x00\x03\x00\x04\x00\x04\x00\x04\x00\xff\xff\xfe\xff\x05\x00\x05\x00\x08\x00\t\x00\t\x00\x08\x00\x08\x00\x07\x00\x05\x00\x05\x00\xff\xff\xfe\xff\xfb\xff\xfa\xff\x06\x00\x07\x00\x08\x00\t\x00\x00\x00\x01\x00\x00\x00\x00\x00\x05\x00\x05\x00\xfd\xff\xfd\xff\x05\x00\x06\x00\x06\x00\x08\x00\xfd\xff\xfc\xff\x03\x00\x02\x00\xfd\xff\xfc\xff\xfd\xff\xfd\xff\x02\x00\x03\x00\x06\x00\x05\x00\x02\x00\x02\x00\x06\x00\x05\x00\x05\x00\x04\x00\xf9\xff\xf9\xff\xfe\xff\xff\xff\x02\x00\x02\x00\x01\x00\x01\x00\x01\x00\x00\x00\x03\x00\x03\x00\x04\x00\x05\x00\x03\x00\x03\x00\x04\x00\x03\x00\x02\x00\x02\x00\x00\x00\x03\x00\x00\x00\x01\x00\x00\x00\xff\xff\x02\x00\x02\x00\t\x00\t\x00\x06\x00\x06\x00\xfe\xff\xff\xff\x04\x00\x04\x00\xff\xff\x00\x00\x01\x00\x00\x00\xff\xff\x00\x00\x00\x00\xff\xff\x03\x00\x05\x00\x02\x00\x02\x00\xff\xff\x00\x00\x01\x00\x02\x00\x02\x00\x02\x00\x05\x00\x06\x00\x04\x00\x03\x00\x01\x00\x02\x00\x04\x00\x04\x00\x06\x00\x07\x00\x0c\x00\x0b\x00\x06\x00\x05\x00\x05\x00\x04\x00\x0b\x00\x0b\x00\x04\x00\x05\x00\x05\x00\x05\x00\x06\x00\x07\x00\x03\x00\x04\x00\x07\x00\x07\x00\xff\xff\x00\x00\x03\x00\x02\x00\x05\x00\x03\x00\x07\x00\x07\x00\x06\x00\x07\x00\x03\x00\x03\x00\x06\x00\x06\x00\x06\x00\x05\x00\x05\x00\x05\x00\x02\x00\x02\x00\x07\x00\x07\x00\x01\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x01\x00\x02\x00\x03\x00\x03\x00\x04\x00\x07\x00\x08\x00\x03\x00\x05\x00\x04\x00\x03\x00\xfe\xff\xfe\xff\xfe\xff\xfe\xff\x02\x00\x01\x00\x06\x00\x05\x00\x07\x00\x06\x00\xfd\xff\xfe\xff\x02\x00\x03\x00\x03\x00\x03\x00\x04\x00\x04\x00\x07\x00\x07\x00\x05\x00\x04\x00\n\x00\n\x00\x03\x00\x04\x00\x03\x00\x04\x00\x08\x00\x08\x00\x06\x00\x06\x00\x07\x00\x06\x00\x0b\x00\x0b\x00\xff\xff\x01\x00\xfd\xff\xfd\xff\x06\x00\x06\x00\x00\x00\xff\xff\t\x00\x08\x00\x07\x00\x07\x00\x06\x00\x06\x00\x06\x00\x06\x00\x00\x00\x01\x00\x01\x00\x01\x00\x03\x00\x02\x00\xff\xff\xff\xff\xff\xff\xfe\xff\x02\x00\x03\x00\x02\x00\x02\x00\x00\x00\x02\x00\xfb\xff\xfc\xff\x00\x00\xfe\xff\xfe\xff\xff\xff\xf7\xff\xf5\xff\x06\x00\x06\x00\x07\x00\t\x00\x00\x00\x00\x00\x08\x00\x08\x00\x01\x00\x01\x00\x03\x00\x03\x00\xfe\xff\xfe\xff\x00\x00\x01\x00\x05\x00\x06\x00\x02\x00\x04\x00\x01\x00\x01\x00\x05\x00\x05\x00\xff\xff\x00\x00\xff\xff\x00\x00\x03\x00\x02\x00\xfe\xff\xfe\xff\x01\x00\x01\x00\x02\x00\x02\x00\xff\xff\xfe\xff\x03\x00\x05\x00\x01\x00\x01\x00\xfa\xff\xfa\xff\x00\x00\xff\xff\x00\x00\x01\x00\x02\x00\x03\x00\x06\x00\x06\x00\x03\x00\x04\x00\x04\x00\x05\x00\x00\x00\x00\x00\xfe\xff\xff\xff\xff\xff\xfe\xff\x00\x00\x00\x00\x01\x00\x01\x00\x06\x00\x06\x00\n\x00\t\x00\x03\x00\x03\x00\x03\x00\x04\x00\x01\x00\x01\x00\x07\x00\x06\x00\n\x00\x0b\x00\x05\x00\x05\x00\x07\x00\x07\x00\x05\x00\x03\x00\x02\x00\x03\x00\x02\x00\x01\x00\xfd\xff\xfd\xff\x06\x00\x06\x00\x0f\x00\x0e\x00\t\x00\t\x00\x01\x00\x01\x00\x01\x00\x01\x00\x05\x00\x04\x00\x01\x00\x02\x00\x05\x00\x05\x00\x05\x00\x03\x00\x07\x00\x07\x00\x05\x00\x04\x00\x0b\x00\x0b\x00\t\x00\n\x00\x03\x00\x03\x00\x08\x00\x07\x00\x07\x00\x07\x00\x05\x00\x04\x00\x06\x00\x06\x00\x0b\x00\n\x00\x00\x00\x00\x00\x08\x00\t\x00\x02\x00\x01\x00\x00\x00\x00\x00\xfb\xff\xfa\xff\xfc\xff\xfb\xff\x00\x00\x00\x00\x05\x00\x05\x00\x07\x00\x05\x00\xff\xff\xfe\xff\x08\x00\x07\x00\x01\x00\x01\x00\x01\x00\x02\x00\x04\x00\x03\x00\x04\x00\x04\x00\x00\x00\x00\x00\xfe\xff\xfe\xff\x03\x00\x04\x00\x04\x00\x05\x00\xfd\xff\xfd\xff\x02\x00\x01\x00\xfd\xff\xfd\xff\xf8\xff\xf9\xff\xfd\xff\xfd\xff\x00\x00\x00\x00\x02\x00\x02\x00\x02\x00\x02\x00\x04\x00\x02\x00\x02\x00\x03\x00\xff\xff\xff\xff\xfc\xff\xfc\xff\xff\xff\xff\xff\x00\x00\x00\x00\x06\x00\x06\x00\x05\x00\x05\x00\x02\x00\x02\x00\x08\x00\t\x00\x07\x00\x06\x00\xfe\xff\xfe\xff\xfe\xff\xff\xff\xfc\xff\xfc\xff\x01\x00\x01\x00\xfd\xff\xfc\xff\xf9\xff\xf8\xff\xfe\xff\xfe\xff\xfc\xff\xfd\xff\xfa\xff\xfb\xff\xfe\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfa\xff\xf9\xff\x00\x00\x00\x00\xfe\xff\xff\xff\xf8\xff\xf8\xff\xff\xff\x00\x00\xff\xff\x00\x00\x01\x00\x02\x00\x00\x00\x00\x00\xf8\xff\xf7\xff\xfb\xff\xfb\xff\xfe\xff\xff\xff\x00\x00\x00\x00\xf8\xff\xf8\xff\xfb\xff\xfb\xff\xfe\xff\xfe\xff\xf6\xff\xf7\xff\x02\x00\x02\x00\xfe\xff\xff\xff\x01\x00\x01\x00\x07\x00\x07\x00\x05\x00\x04\x00\x03\x00\x02\x00\xfb\xff\xfc\xff\xfd\xff\xfd\xff\xfd\xff\xfd\xff\xfb\xff\xfd\xff\xfe\xff\xfe\xff\x03\x00\x03\x00\x00\x00\xff\xff\x01\x00\x01\x00\xf9\xff\xf9\xff\xf7\xff\xf7\xff\xfa\xff\xf9\xff\xf6\xff\xf6\xff\x02\x00\x01\x00\xfd\xff\xfd\xff\xfe\xff\xfe\xff\x02\x00\x00\x00\x00\x00\xff\xff\xfc\xff\xfd\xff\x01\x00\x00\x00\x01\x00\x00\x00\xfe\xff\xfe\xff\x04\x00\x04\x00\x02\x00\x03\x00\xff\xff\xfe\xff\xf8\xff\xf7\xff\xf6\xff\xf6\xff\xf9\xff\xf9\xff\xfc\xff\xfc\xff\xfc\xff\xfc\xff\xff\xff\xfe\xff\xff\xff\xfe\xff\xfb\xff\xfb\xff\xfd\xff\x00\x00\x01\x00\x00\x00\xfa\xff\xfb\xff\xfe\xff\xfe\xff\xfc\xff\xfd\xff\x02\x00\x01\x00\xff\xff\x00\x00\xfd\xff\xfd\xff\xfd\xff\xfe\xff\xfd\xff\xfd\xff\xf9\xff\xf9\xff\xff\xff\xff\xff\xfe\xff\xff\xff\xfc\xff\xfc\xff\x04\x00\x04\x00\xfd\xff\xfd\xff\x01\x00\x01\x00\xfb\xff\xfb\xff\xfb\xff\xfb\xff\x01\x00\x00\x00\xfb\xff\xfc\xff\xfa\xff\xfb\xff\xfe\xff\xfe\xff\x04\x00\x03\x00\x03\x00\x02\x00\xf8\xff\xf9\xff\xff\xff\xfe\xff\xff\xff\x00\x00\x01\x00\x00\x00\x07\x00\x07\x00\x01\x00\x01\x00\xfb\xff\xfa\xff\xff\xff\x01\x00\x05\x00\x06\x00\xfe\xff\xff\xff\xfe\xff\xfe\xff\xff\xff\xff\xff\xfc\xff\xfb\xff\xff\xff\xfe\xff\xff\xff\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\xf8\xff\xf8\xff\xfd\xff\xfe\xff\x00\x00\x01\x00\xfd\xff\xfe\xff\xfb\xff\xfb\xff\xff\xff\xff\xff\x00\x00\x00\x00\xfb\xff\xfb\xff\xf9\xff\xf9\xff\xfd\xff\xfd\xff\xfc\xff\xfc\xff\xfe\xff\xff\xff\xff\xff\xfe\xff\xf9\xff\xf9\xff\xfb\xff\xfc\xff\xfa\xff\xfa\xff\xf6\xff\xf8\xff\xf7\xff\xf8\xff\xf6\xff\xf6\xff\xfb\xff\xfb\xff\xfe\xff\xfe\xff\xfb\xff\xfa\xff\xfb\xff\xfc\xff\xfc\xff\xfb\xff\xfc\xff\xfb\xff\x01\x00\x01\x00\x02\x00\x02\x00\x00\x00\x00\x00\xfd\xff\xfd\xff\x00\x00\x01\x00\xff\xff\xff\xff\xfd\xff\xfc\xff\x01\x00\x01\x00\x05\x00\x07\x00\x01\x00\x01\x00\x04\x00\x04\x00\xff\xff\xfe\xff\xf9\xff\xf9\xff\xfe\xff\xfd\xff\xfb\xff\xf9\xff\x00\x00\x01\x00\x01\x00\x00\x00\xfc\xff\xfc\xff\x04\x00\x03\x00\xff\xff\x01\x00\x00\x00\x00\x00\x03\x00\x03\x00\x00\x00\x00\x00\x03\x00\x01\x00\x01\x00\x02\x00\x07\x00\x05\x00\x05\x00\x05\x00\xfe\xff\xff\xff\xff\xff\xff\xff\x01\x00\x01\x00\xfd\xff\xff\xff\x01\x00\xff\xff\x04\x00\x04\x00\x01\x00\x02\x00\x00\x00\x01\x00\xfb\xff\xfc\xff\xfb\xff\xfb\xff\x02\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x04\x00\x04\x00\x06\x00\x06\x00\x06\x00\x07\x00\x06\x00\x06\x00\x00\x00\xff\xff\x03\x00\x03\x00\x05\x00\x06\x00\xfb\xff\xfa\xff\xf6\xff\xf5\xff\xfa\xff\xfa\xff\x01\x00\x01\x00\xff\xff\x00\x00\x00\x00\x01\x00\x08\x00\x07\x00\xfc\xff\xfc\xff\xfb\xff\xfc\xff\x02\x00\x01\x00\xff\xff\xff\xff\x00\x00\x00\x00\xff\xff\xfe\xff\x07\x00\x06\x00\x05\x00\x05\x00\x03\x00\x03\x00\x02\x00\x02\x00\xfb\xff\xfb\xff\x04\x00\x04\x00\x03\x00\x03\x00\xfd\xff\xfe\xff\x03\x00\x03\x00\xfc\xff\xfb\xff\xfd\xff\xfe\xff\x01\x00\xff\xff\xf8\xff\xf7\xff\xfa\xff\xfa\xff\x00\x00\xff\xff\xfe\xff\xff\xff\x00\x00\x00\x00\x08\x00\x07\x00\x02\x00\x02\x00\x00\x00\x00\x00\x01\x00\x01\x00\xfd\xff\xff\xff\xfa\xff\xf9\xff\x00\x00\xfe\xff\xfe\xff\xfd\xff\xfe\xff\xfe\xff\xff\xff\x00\x00\xff\xff\xff\xff\x00\x00\x01\x00\x00\x00\x02\x00\xfd\xff\xfc\xff\xfd\xff\xfd\xff\xfc\xff\xfc\xff\xfb\xff\xfc\xff\xfd\xff\xfc\xff\x00\x00\xff\xff\x04\x00\x04\x00\x01\x00\x01\x00\xfe\xff\xff\xff\xf7\xff\xf8\xff\x03\x00\x03\x00\x06\x00\x06\x00\x04\x00\x05\x00\x03\x00\x03\x00\xfb\xff\xfa\xff\x00\x00\xff\xff\xfa\xff\xfa\xff\xfc\xff\xfc\xff\x06\x00\x06\x00\xfb\xff\xfb\xff\xf8\xff\xf9\xff\xfe\xff\xfe\xff\x01\x00\xff\xff\x00\x00\xff\xff\xfc\xff\xfb\xff\xfa\xff\xfa\xff\xfc\xff\xfc\xff\xfb\xff\xfa\xff\x02\x00\x01\x00\x05\x00\x04\x00\n\x00\n\x00\x05\x00\x06\x00\xff\xff\xfd\xff\xfe\xff\xfe\xff\xfe\xff\xfe\xff\xfe\xff\xff\xff\x00\x00\x01\x00\x04\x00\x05\x00\xff\xff\xff\xff\x01\x00\x02\x00\x07\x00\x06\x00\x01\x00\x02\x00\xfd\xff\xfe\xff\xff\xff\xff\xff\x00\x00\x00\x00\xf9\xff\xfa\xff\x01\x00\x02\x00\x05\x00\x05\x00\x05\x00\x05\x00\x03\x00\x02\x00\xf8\xff\xf7\xff\xfc\xff\xfc\xff\xfd\xff\xfd\xff\x04\x00\x03\x00\x07\x00\x07\x00\x06\x00\x06\x00\x02\x00\x03\x00\x06\x00\x07\x00\x07\x00\x07\x00\x04\x00\x03\x00\x02\x00\x01\x00\xfe\xff\xfc\xff\x01\x00\x01\x00\x02\x00\x02\x00\x02\x00\x03\x00\xfd\xff\xfe\xff\x08\x00\x08\x00\x03\x00\x01\x00\xfe\xff\xfe\xff\x07\x00\x08\x00\x04\x00\x06\x00\xfe\xff\xfe\xff\x01\x00\x01\x00\x01\x00\x01\x00\x04\x00\x05\x00\r\x00\x0c\x00\x04\x00\x04\x00\xff\xff\xfe\xff\xfd\xff\xfc\xff\x07\x00\x08\x00\x05\x00\x06\x00\x00\x00\x00\x00\xff\xff\xff\xff\xfe\xff\xfe\xff\xfe\xff\xfe\xff\x01\x00\x00\x00\x01\x00\x00\x00\x03\x00\x02\x00\x05\x00\x04\x00\x00\x00\x01\x00\xfd\xff\xfc\xff\x00\x00\xfd\xff\x00\x00\x00\x00\x02\x00\xff\xff\x06\x00\x06\x00\x02\x00\x01\x00\xfb\xff\xfa\xff\xff\xff\xff\xff\x01\x00\x01\x00\xf8\xff\xf7\xff\x00\x00\x00\x00\xfe\xff\xfc\xff\xf9\xff\xf8\xff\xff\xff\xff\xff\xfe\xff\xfd\xff\xff\xff\xff\xff\x03\x00\x02\x00\x05\x00\x03\x00\xfd\xff\xff\xff\x01\x00\x02\x00\x02\x00\x03\x00\x03\x00\x03\x00\x01\x00\x02\x00\t\x00\x08\x00\n\x00\t\x00\x02\x00\x03\x00\x04\x00\x04\x00\x07\x00\x08\x00\n\x00\t\x00\x08\x00\x08\x00\x08\x00\t\x00\x00\x00\x02\x00\x06\x00\x05\x00\x04\x00\x05\x00\x08\x00\x08\x00\x06\x00\x07\x00\x03\x00\x04\x00\x06\x00\x08\x00\xfa\xff\xfb\xff\x01\x00\x02\x00\x07\x00\x06\x00\x02\x00\x02\x00\x03\x00\x02\x00\x04\x00\x04\x00\x04\x00\x06\x00\x06\x00\x06\x00\x05\x00\x04\x00\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\xff\xff\x01\x00\x00\x00\x01\x00\x01\x00\x02\x00\x02\x00\x06\x00\x06\x00\x00\x00\xfe\xff\xfe\xff\x00\x00\x08\x00\t\x00\x07\x00\x07\x00\x04\x00\x03\x00\x06\x00\x04\x00\r\x00\x0f\x00\x0c\x00\n\x00\x04\x00\x05\x00\x07\x00\x06\x00\t\x00\x08\x00\x07\x00\x06\x00\n\x00\n\x00\x07\x00\x07\x00\x05\x00\x05\x00\x04\x00\x04\x00\x02\x00\x03\x00\x07\x00\x08\x00\x08\x00\x08\x00\x07\x00\x08\x00\x07\x00\x06\x00\x02\x00\x04\x00\x07\x00\x07\x00\x04\x00\x03\x00\x01\x00\x01\x00\x0b\x00\x0e\x00\x01\x00\x01\x00\x00\x00\x00\x00\x02\x00\x02\x00\x03\x00\x01\x00\x03\x00\x02\x00\x05\x00\x05\x00\x00\x00\x00\x00\xfc\xff\xfa\xff\x05\x00\x04\x00\x03\x00\x04\x00\x05\x00\x06\x00\x01\x00\x01\x00\x02\x00\x02\x00\xff\xff\x00\x00\xfc\xff\xfc\xff\x02\x00\x02\x00\x00\x00\xff\xff\xff\xff\x00\x00\x01\x00\x01\x00\x04\x00\x03\x00\xff\xff\x00\x00\x00\x00\xff\xff\xfb\xff\xfb\xff\x00\x00\x00\x00\x03\x00\x04\x00\x05\x00\x06\x00\x06\x00\x08\x00\x03\x00\x04\x00\x06\x00\x04\x00\xfe\xff\xfe\xff\x02\x00\x03\x00\x05\x00\x04\x00\x03\x00\x03\x00\x07\x00\x07\x00\x02\x00\x03\x00\x01\x00\x00\x00\x03\x00\x04\x00\x07\x00\x08\x00\x05\x00\x05\x00\x06\x00\x06\x00\x06\x00\x06\x00\x0c\x00\x0b\x00\x08\x00\x08\x00\xfe\xff\xff\xff\x06\x00\x05\x00\x02\x00\x02\x00\xfe\xff\xfe\xff\xfe\xff\xff\xff\x05\x00\x06\x00\x01\x00\x00\x00\x02\x00\x01\x00\x03\x00\x03\x00\x04\x00\x04\x00\xff\xff\xff\xff\xff\xff\xfe\xff\x03\x00\x02\x00\xfa\xff\xfb\xff\x03\x00\x02\x00\x05\x00\x06\x00\x05\x00\x05\x00\x06\x00\x05\x00\x07\x00\x07\x00\x08\x00\x06\x00\x03\x00\x02\x00\x00\x00\x01\x00\x05\x00\x05\x00\x00\x00\x01\x00\xfc\xff\xfd\xff\xff\xff\x00\x00\x03\x00\x03\x00\x04\x00\x03\x00\x01\x00\x01\x00\x05\x00\x05\x00\x04\x00\x04\x00\x05\x00\x05\x00\x06\x00\x05\x00\x08\x00\x08\x00\x08\x00\t\x00\x06\x00\x05\x00\x05\x00\x05\x00\x0c\x00\x0b\x00\x08\x00\t\x00\x02\x00\x01\x00\x08\x00\x08\x00\x08\x00\t\x00\xff\xff\xff\xff\x05\x00\x04\x00\x03\x00\x03\x00\xfc\xff\xfc\xff\xfe\xff\x00\x00\xf9\xff\xf9\xff\xfe\xff\xfe\xff\xfd\xff\xfd\xff\xfc\xff\xfb\xff\x00\x00\xff\xff\xff\xff\x00\x00\xfb\xff\xfb\xff\x00\x00\x00\x00\xf9\xff\xf9\xff\xfb\xff\xfc\xff\x02\x00\x00\x00\x00\x00\x01\x00\xfd\xff\xfd\xff\x00\x00\x00\x00\xfb\xff\xfb\xff\xf2\xff\xf2\xff\x01\x00\x01\x00\xff\xff\x00\x00\xfe\xff\xfe\xff'"
#set callbak for audio record
def callback(in_data, frame_count, time_info, status):
    try:
        if(sys.getsizeof(in_data)>0):
            wf.writeframes(in_data)
            audio_tmp=in_data
        else:
            in_data=audio_tmp
            wf.writeframes(in_data)
    except:
        pass
    else:
        if audio_record_flag:
            return (in_data, pyaudio.paContinue)
        else:
            return (in_data, pyaudio.paComplete)

#set stream get audio
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                input=True,
                stream_callback=callback)


#get screen info and get screem image
image = ImageGrab.grab()
width = image.size[0]
height = image.size[1]
print("width:", width, "height:", height)
print("image mode:",image.mode)
k=np.zeros((width,height),np.uint8)

#set video image  base XVID
fourcc = cv2.VideoWriter_fourcc(*'XVID')

#文件名，编码，帧数，获取的图像大小
#若设置帧率与实际帧率不一致，会导致视频时间与音频时间不一致 ,VIDEO_FREAME between 1 to 10.
video = cv2.VideoWriter(VIDEO_OUTPUT_FILENAME, fourcc, VIDEO_FREAME, (width, height))

#start record audio
print("start audio recording!!!!!")
stream.start_stream()

#start record video
print("start video recording!!!!!")
img_bgr=0
while True:
    try:
        img_rgb = ImageGrab.grab()

        if (sys.getsizeof(img_rgb) >0):
            try:
                img_bgr=cv2.cvtColor(np.array(img_rgb), cv2.COLOR_RGB2BGR)#转为opencv的BGR格式
            except:
                pass
            else:
                if (sys.getsizeof(img_bgr) >0):
                    video.write(img_bgr)
                else:
                    pass
        else:
            pass
    except KeyboardInterrupt:   # ctrl+c
        audio_record_flag = False
        stream.stop_stream()
        stream.close()
        wf.close()
        video.release()

        p.terminate()
        cv2.destroyAllWindows()

        print("break all recording")
        break
     

#merge audio and video,the vidoe and audio time axit is different ,so it not usefull.
# print("video audio merge!!!!!")
# audioclip = AudioFileClip(WAVE_OUTPUT_FILENAME)
# videoclip = VideoFileClip(VIDEO_OUTPUT_FILENAME)
# videoclip2 = videoclip.set_audio(audioclip)
# video = CompositeVideoClip([videoclip2])
# video.write_videofile("test2.mp4",codec='mpeg4')