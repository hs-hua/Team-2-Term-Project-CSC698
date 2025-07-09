import tkinter as tk
from tkinter import messagebox, scrolledtext, END
import enchant
import random

# Global variable to hold the locked word
_locked_word = None

# Dictionary to validate real English words
dictionary = enchant.Dict("en_US")

# Sample questions for the game
sample_questions = [
    "Is it a living thing?",
    "Is it something you can eat?",
    "Is it an object?",
    "Is it a place?",
    "Is it something you can buy?",
    "Is it bigger than a loaf of bread?",
    "Is it used daily?",
    "Is it found indoors?",
    "Is it made by humans?",
    "Is it a proper noun?",
    "Does it have more than one syllable?",
    "Is it something you wear?",
    "Can it be found in nature?",
    "Is it something that makes noise?",
    "Is it a feeling or emotion?",
    "Is it something you use with your hands?",
    "Is it electronic?",
    "Is it found in a school?",
    "Is it part of your body?",
    "Is it related to technology?"
]

# Game state
questions_asked = 0
guesses_made = 0
max_questions = 20
max_guesses = 3


# ------------------- Step 1: Lock Word GUI -------------------

def lock_word():
    global _locked_word
    user_word = entry.get().strip().lower()

    if not dictionary.check(user_word):
        messagebox.showerror("Invalid Word", "That is not a valid English word.")
        return

    _locked_word = user_word
    messagebox.showinfo("Word Locked", "Your word has been locked in securely.")
    lock_window.destroy()
    start_game_gui()


lock_window = tk.Tk()
lock_window.title("Enter Secret Word")
lock_window.geometry("400x150")

label = tk.Label(lock_window, text="Enter a real English word:")
label.pack(pady=10)

entry = tk.Entry(lock_window, show="*", width=30)
entry.pack()

lock_button = tk.Button(lock_window, text="Lock Word", command=lock_word)
lock_button.pack(pady=10)

lock_window.mainloop()


# ------------------- Step 2: Game GUI -------------------

def get_chatbot_response(user_input):
    global questions_asked, guesses_made

    user_input = user_input.strip().lower()

    if questions_asked < max_questions:
        if user_input in ['yes', 'no']:
            questions_asked += 1
            if questions_asked < len(sample_questions):
                next_question = sample_questions[questions_asked]
            else:
                next_question = f"Custom question {questions_asked + 1}: Is it helpful?"
            return f"Question {questions_asked + 1}: {next_question}"
        elif "guess" in user_input and guesses_made < max_guesses:
            guess_word = user_input.replace("guess", "").strip()
            guesses_made += 1
            if guess_word == _locked_word:
                return "🎉 Correct! The system guessed your word!"
            else:
                return f"❌ Incorrect guess ({guesses_made}/{max_guesses})."
        else:
            return "Please respond with 'yes', 'no', or allow a guess using 'guess <word>'."
    else:
        return f"❗ Maximum of {max_questions} questions reached. The word was: {_locked_word}"


def show_chatbot_response():
    user_input = user_input_box.get("1.0", END).strip()
    user_input_box.delete("1.0", END)

    if user_input.lower() in ["exit", "quit", "bye"]:
        chat_log.insert(tk.END, "Chatbot: Goodbye!\n")
        return

    chat_log.insert(tk.END, "You: " + user_input + "\n")
    chatbot_response = get_chatbot_response(user_input)
    chat_log.insert(tk.END, "Chatbot: " + chatbot_response + "\n")


def start_game_gui():
    global chat_log, user_input_box

    game_root = tk.Tk()
    game_root.title("The 20 Questions Game")

    chat_log = scrolledtext.ScrolledText(game_root, width=60, height=20, wrap=tk.WORD)
    chat_log.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    user_input_box = scrolledtext.ScrolledText(game_root, width=40, height=4, wrap=tk.WORD)
    user_input_box.grid(row=1, column=0, padx=10, pady=10)

    send_button = tk.Button(game_root, text="Send", command=show_chatbot_response)
    send_button.grid(row=1, column=1, padx=10, pady=10)

    # Start with the first question
    chat_log.insert(tk.END, f"Chatbot: Question 1: {sample_questions[0]}\n")

    game_root.mainloop()
