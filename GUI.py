from tkinter import *
from PIL import Image, ImageTk


root = Tk()
root.title("Cerebro")
root.geometry("600x400")
root.configure(bg="#1e1e1e")

frame = Frame(root, bg="#1e1e1e")
frame.pack(fill="both", expand=True)

text = Label(
    frame,
    text="Welcome to Cerebro",
    font=("Arial", 20),
    bg="#1e1e1e",
    fg="white"
)


text.pack(pady=(40, 0))

root.mainloop()