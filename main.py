import pvporcupine
from pvrecorder import PvRecorder
from rich import print
import time
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'sound'))
from sound.play import play
from config.vosk_modul import vosk_modul
from config.porcupine_config import *

# Инициализация Porcupine
porcupine = pvporcupine.create(
    access_key=access_key,
    keyword_paths=keyword_paths
)

# Инициализация микрофона
recorder = PvRecorder(device_index=0, frame_length=porcupine.frame_length)
recorder.start()

print("Jarvis V2 has been started")
play("Run")
print("I wait 'Jarvis'...")

# Основной цикл
try:
    while True:
        audio_frame = recorder.read()
        keyword_index = porcupine.process(audio_frame)

        if keyword_index >= 0:
            print("Detected 'Jarvis'")
            play("Shazam-ON")
            recorder.stop()
            vosk_modul()

            recorder.start()
            lts = time.time()
            play("Shazam-OFF")
            print("I wait 'Jarvis'...")

except KeyboardInterrupt:
    print("Stopping...")

finally:
    try:
        recorder.stop()
        recorder.delete()
    except Exception:
        pass
    porcupine.delete()
