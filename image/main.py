import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()

path = "C:/Users/artko/python/image/reflection.png"

img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(root, image=img)
panel.pack(side="bottom", fill="both", expand="no")
root.mainloop()
