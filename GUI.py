from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Ai Assistant")
root.geometry("538x713")
root.configure(bg="#7693B2")
root.resizable(False, False)

main_frame = Frame(
    root,
    bg="#7693B2",
    highlightthickness=2,
    highlightbackground="#4A6985"
)
main_frame.place(x=20, y=45, width=498, height=625)

title_label = Label(
    main_frame,
    text="AI Assistant",
    font=("Arial", 22, "bold"),
    bg="#53789D",
    fg="black",
    padx=10,
    pady=3
)
title_label.place(x=165, y=16)

image_area = Frame(main_frame, bg="white")
image_area.place(x=102, y=83, width=294, height=260)

image = ImageTk.PhotoImage(Image.open("image/ai.png").resize((230, 230)))
image_label = Label(image_area, image=image, bg="white", bd=0)
image_label.place(relx=0.5, rely=0.5, anchor="center")

chat_box = Text(
    main_frame,
    font=("Arial", 12),
    bg="#3A6695",
    fg="white",
    bd=2,
    relief="solid",
    highlightthickness=0,
    insertbackground="white",
    wrap="word"
)
chat_box.place(x=43, y=385, width=412, height=100)
chat_box.insert("end", "Hello, I am your AI Assistant.\n")
chat_box.configure(state="disabled")

message_var = StringVar()


def send_message():
    message = message_var.get().strip()
    if message:
        chat_box.configure(state="normal")
        chat_box.insert("end", f"You: {message}\n")
        chat_box.see("end")
        chat_box.configure(state="disabled")
        message_var.set("")


def ask_message():
    send_message()


def delete_message():
    message_var.set("")


message_entry = Entry(
    main_frame,
    textvariable=message_var,
    font=("Arial", 12),
    bg="#ECECEC",
    fg="black",
    bd=1,
    relief="solid",
    highlightthickness=0,
    insertbackground="black"
)
message_entry.place(x=43, y=510, width=412, height=36)

ask_btn = Button(
    main_frame,
    text="ASK",
    font=("Arial", 12, "bold"),
    bg="#2E608E",
    fg="black",
    activebackground="#2E608E",
    activeforeground="black",
    bd=2,
    relief="solid",
    command=ask_message
)
ask_btn.place(x=43, y=560, width=120, height=50)

delete_btn = Button(
    main_frame,
    text="DELETE",
    font=("Arial", 12, "bold"),
    bg="#2E608E",
    fg="black",
    activebackground="#2E608E",
    activeforeground="black",
    bd=2,
    relief="solid",
    command=delete_message
)
delete_btn.place(x=189, y=560, width=120, height=50)

send_btn = Button(
    main_frame,
    text="SEND",
    font=("Arial", 12, "bold"),
    bg="#2E608E",
    fg="black",
    activebackground="#2E608E",
    activeforeground="black",
    bd=2,
    relief="solid",
    command=send_message
)
send_btn.place(x=335, y=560, width=120, height=50)

message_entry.bind("<Return>", lambda _event: send_message())
message_entry.focus_set()

root.mainloop()
