import os
import random
from playsound import playsound
import threading

# Асинхронное воспроизведение звука
def play(phrase):
    def _play():
        mapping = {
            "Hi": f"greet{random.choice([1, 2, 3])}",
            "Ok": f"ok{random.choice([1, 2, 3, 4])}",
            "Thanks": "thanks",
            "Stupid": "stupid",
            "OFF-system": "off",
            "Run": "run",
            "Shazam-ON": "Shazam-Detected",
            "Shazam-OFF": "Shazam-Detected-rev"
        }

        base = mapping.get(phrase, phrase)
        package_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        filename = os.path.join(package_dir, "sound", "jarvis-og", f"{base}.wav")

        if not os.path.exists(filename):
            print(f"Файл не найден: {filename}")
            return

        try:
            playsound(filename, block=False)
        except Exception as e:
            print(f"Ошибка воспроизведения: {e}")

    threading.Thread(target=_play, daemon=True).start()