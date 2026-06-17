# ================================================
# PROJECT 1: RULE-BASED AI CHATBOT (GUI Version)
# DecodeLabs Industrial Training Kit - Batch 2026
# ================================================

import tkinter as tk
from tkinter import scrolledtext

# Knowledge Base
responses = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! Nice to meet you.",
    "hey": "Hey! What's going on?",
    "how are you": "I'm functioning perfectly. How about you?",
    "what is your name": "I'm DecodeBot, your rule-based AI assistant from DecodeLabs.",
    "who are you": "I'm a Rule-Based Chatbot developed for DecodeLabs AI Training Program.",
    "thank you": "You're very welcome.",
    "thanks": "My pleasure.",
    "good morning": "Good morning! Wishing you a great day ahead.",
    "good evening": "Good evening! Hope you're having a wonderful day.",
    "good night": "Good night! Sweet dreams.",
    "joke": "Why do programmers prefer dark mode? Because light attracts bugs.",
    "weather": "I can't check real weather yet, but in the world of code it's always sunny with a chance of bugs.",
    "bye": "Goodbye! Have a fantastic day.",
    "goodbye": "Goodbye! It was nice chatting with you.",
}

class ChatbotGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("DecodeBot - Rule-Based AI Chatbot")
        self.root.geometry("700x500")
        self.root.configure(bg="#1e1e2e")

        # Title
        title = tk.Label(self.root, text="🤖 DecodeBot - Rule-Based AI Chatbot", 
                        font=("Arial", 16, "bold"), bg="#1e1e2e", fg="#00ff9d")
        title.pack(pady=10)

        # Chat Display
        self.chat_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, 
                                                  font=("Consolas", 11), bg="#2d2d44", fg="#ffffff")
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        self.chat_area.config(state='disabled')

        # Input Frame
        input_frame = tk.Frame(self.root, bg="#1e1e2e")
        input_frame.pack(padx=10, pady=5, fill=tk.X)

        self.user_input = tk.Entry(input_frame, font=("Consolas", 11), bg="#3d3d5c", fg="#ffffff")
        self.user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        self.user_input.bind("<Return>", self.send_message)

        send_button = tk.Button(input_frame, text="Send", command=self.send_message,
                               bg="#00ff9d", fg="black", font=("Arial", 10, "bold"), width=10)
        send_button.pack(side=tk.RIGHT)

        # Welcome Message
        self.display_message("DecodeBot", "Hello! I am DecodeBot - a Rule-Based AI Chatbot.\nType your message below...", "#00ff9d")

    def display_message(self, sender, message, color="#ffffff"):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, f"{sender}: {message}\n\n", )
        self.chat_area.tag_config(sender, foreground=color)
        self.chat_area.see(tk.END)
        self.chat_area.config(state='disabled')

    def send_message(self, event=None):
        user_text = self.user_input.get().strip()
        if not user_text:
            return

        self.display_message("You", user_text, "#a0a0ff")
        self.user_input.delete(0, tk.END)

        clean_input = user_text.lower()

        # Exit Command
        if clean_input in ["exit", "quit", "bye", "goodbye"]:
            self.display_message("DecodeBot", "Goodbye! Keep mastering AI.", "#00ff9d")
            self.root.after(1500, self.root.quit)
            return

        # Get Response
        reply = responses.get(clean_input)

        if reply:
            self.display_message("DecodeBot", reply, "#00ff9d")
        else:
            self.display_message("DecodeBot", "I don't have a predefined rule for that.", "#ffaa00")
            self.display_message("DecodeBot", "→ Would pass to LLM for generative response (Hybrid Architecture)", "#ffaa00")
            
            # Additional Smart Logic
            if "how" in clean_input:
                self.display_message("DecodeBot", "I'm great at following rules. What would you like to know?", "#00ff9d")
            elif any(word in clean_input for word in ["age", "old", "born", "created"]):
                self.display_message("DecodeBot", "I was created as part of this DecodeLabs training project.", "#00ff9d")

if __name__ == "__main__":
    app = ChatbotGUI()
    app.root.mainloop()
