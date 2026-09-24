import tkinter as tk
import tkinter.font as tkfont
import subprocess

root = tk.Tk()

default_font = tkfont.nametofont("TkDefaultFont")
default_font.configure(size=36)

root.title("voice-mixer v.01")

root.geometry("750x200+1000+250")
root.resizable(False, True)

root.attributes("-topmost", True)
root.attributes("-alpha", "0.9")


# def key_handler(event):
#     print(event.char, event.keysym, event.keycode)


# root.bind("<Key>", key_handler)


def change_volume(action):
    if action == "+":
        command = "nircmd.exe changesysvolume +5000"
        subprocess.run(command)
    elif action == "-":
        command = "nircmd.exe changesysvolume -5000"
        subprocess.run(command)


def stop_playing(event):
    command = "nircmd.exe sendkey 0xB3 press"
    subprocess.run(command)


def next_track():
    command = "nircmd.exe sendkey 0xB0 press"
    subprocess.run(command)


def previous_track():
    command = "nircmd.exe sendkey 0xB1 press"
    subprocess.run(command)


def set_default_sound(speakers, headphones):
    command = "nircmd.exe setdefaultsounddevice"


plus_btn = tk.Button(text="+", command=lambda: change_volume("+"))
# plus_btn.bind("<Button-1>", change_volume("+"))


minus_btn = tk.Button(text="-", command=lambda: change_volume("-"))
# minus_btn.bind("<Button-1>", lambda: change_volume("-"))

previous_btn = tk.Button(text="⏮️", command=previous_track)
# stop_btn = tk.Button(text="▶", command=stop_playing)
stop_btn = tk.Button(text="▶")
stop_btn.bind("<Button-1>", stop_playing)

next_btn = tk.Button(text="⏭️", command=next_track)

speakers = tk.Button(text="🔊")
speakers.bind("<Button-1>", set_default_sound)


headphones = tk.Button(text="🎧")

CONTROLS = [plus_btn, minus_btn, previous_btn, stop_btn, next_btn, speakers, headphones]

for item in CONTROLS:
    item = item.pack(side=tk.LEFT, padx=5, pady=5)


root.mainloop()
