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

message_var = StringVar()


def send_message():
    message = message_var.get().strip()
    if message:
        print(f"Message sent: {message}")
        message_var.set("")


message_entry = Entry(
    frame,
    textvariable=message_var,
    font=("Arial", 12),
    width=28,
    bd=2
)
message_entry.place(x=150, y=320)

send_btn = Button(
    frame,
    text="Send",
    font=("Arial", 11, "bold"),
    bg="#2d89ef",
    fg="white",
    bd=0,
    padx=14,
    pady=4,
    command=send_message
)
send_btn.place(x=410, y=317)

root.mainloop()
