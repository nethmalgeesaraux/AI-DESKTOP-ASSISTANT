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


input_row = Frame(frame, bg="#1e1e1e")
input_row.place(x=75, y=315, width=450, height=40)

message_entry = Entry(
    input_row,
    textvariable=message_var,
    font=("Arial", 12),
    bd=0,
    relief="flat",
    highlightthickness=1,
    highlightbackground="#8a8a8a",
    highlightcolor="#8a8a8a",
    insertbackground="black"
)
message_entry.place(x=0, y=0, width=340, height=40)

send_btn = Button(
    input_row,
    text="Send",
    font=("Arial", 12, "bold"),
    bg="#2d89ef",
    fg="white",
    activebackground="#2d89ef",
    activeforeground="white",
    bd=0,
    command=send_message
)
send_btn.place(x=344, y=0, width=106, height=40)

root.mainloop()
