import subprocess
import os
CDIR = os.getcwd()

commands = {
    "телеграм": lambda: subprocess.Popen([f"{CDIR}\\command_sets\\Run Telegram.exe"]),
    "браузер": lambda: subprocess.Popen([f"{CDIR}\\command_sets\\Run Browser.exe"]),
    "выключи компьютер": lambda: subprocess.Popen([f"{CDIR}\\command_sets\\Close system.exe"]),
    "перезагрузи компьютер": lambda: subprocess.Popen([f'{CDIR}\\command_sets\\Reset system.exe']),
    "ютуб": lambda: subprocess.Popen([f'{CDIR}\\command_sets\\Run YouTube.exe']),
    "музыка": lambda: subprocess.Popen([f'{CDIR}\\command_sets\\Run Music.exe']),
    "режим без звука": lambda: subprocess.Popen([f'{CDIR}\\command_sets\\Off Sounds.exe']),
    "верни звук": lambda: subprocess.Popen([f'{CDIR}\\command_sets\\On Sounds.exe']),
    "громче": lambda: subprocess.Popen([f'{CDIR}\\command_sets\\Sounds Up.exe']),
    "тише": lambda: subprocess.Popen([f'{CDIR}\\command_sets\\Sounds Down.exe']),
    "дальше": lambda: subprocess.Popen([f'{CDIR}\\command_sets\\Next Track.exe']),
    "назад": lambda: subprocess.Popen([f'{CDIR}\\command_sets\\Prev Track.exe']),
    "стоп": lambda: subprocess.Popen([f'{CDIR}\\command_sets\\Stop-Start.exe']),
    "старт": lambda: subprocess.Popen([f'{CDIR}\\command_sets\\Stop-Start.exe'])
}
