import anthropic
import os
import tkinter as tk
from tkinter import scrolledtext
from dotenv import load_dotenv

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))


def send_message():
    user_message = input_field.get()
    if not user_message:
        return

    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, "You: " + user_message + "\n\n")
    input_field.delete(0, tk.END)

    message = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=[{"role": "user", "content": user_message}]
    )

    response = message.content[0].text
    chat_area.insert(tk.END, "Bot: " + response + "\n\n")
    chat_area.config(state=tk.DISABLED)
    chat_area.see(tk.END)


# Build the window
window = tk.Tk()
window.title("AI Chatbot")
window.geometry("600x500")
window.configure(bg="#1a1a2e")

title = tk.Label(window, text="AI Chatbot", font=(
    "Arial", 18, "bold"), bg="#1a1a2e", fg="#00d4ff")
title.pack(pady=10)

chat_area = scrolledtext.ScrolledText(
    window, state=tk.DISABLED, wrap=tk.WORD, bg="#16213e", fg="white", font=("Arial", 11))
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

frame = tk.Frame(window, bg="#1a1a2e")
frame.pack(fill=tk.X, padx=10, pady=10)

input_field = tk.Entry(frame, font=("Arial", 12), bg="#16213e", fg="white")
input_field.pack(side=tk.LEFT, fill=tk.X, expand=True, ipady=8)
input_field.bind("<Return>", lambda e: send_message())

send_btn = tk.Button(frame, text="Send", font=(
    "Arial", 12, "bold"), bg="#00d4ff", fg="black", command=send_message)
send_btn.pack(side=tk.RIGHT, padx=5)

window.mainloop()
