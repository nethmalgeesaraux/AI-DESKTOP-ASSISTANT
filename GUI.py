from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Cerebro")
root.geometry("600x400")
root.configure(bg="#1e1e1e")
root.resizable(False, False)

frame = Frame(root, bg="#1e1e1e")
frame.pack(fill="both", expand=True)


image = ImageTk.PhotoImage(
    Image.open("image/ai.png").resize((200, 200))
)

image_label = Label(frame, image=image, bg="#1e1e1e")
image_label.place(x=200, y=80)


text = Label(
    frame,
    text="Welcome to Cerebro",
    font=("Arial", 20, "bold"),
    bg="#1e1e1e",
    fg="white"
)

text.place(x=170, y=250)

root.mainloop()