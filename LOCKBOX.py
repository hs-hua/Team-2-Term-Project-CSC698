import tkinter as tk
from tkinter import messagebox
import enchant

# Global variable to hold the locked word privately
_locked_word = None

# Dictionary to check real English words
dictionary = enchant.Dict("en_US")

# GUI to get the secret word
def lock_word():
    global _locked_word
    user_word = entry.get().strip().lower()

    if not dictionary.check(user_word):
        messagebox.showerror("Invalid Word", "That is not a valid English word.")
        return

    _locked_word = user_word
    messagebox.showinfo("Word Locked", "Your word has been locked in securely.")
    root.destroy()  # Close GUI and continue in terminal

# GUI Setup
root = tk.Tk()
root.title("Enter Secret Word")
root.geometry("400x150")

label = tk.Label(root, text="Enter a real English word:")
label.pack(pady=10)

entry = tk.Entry(root, show="*", width=30)
entry.pack()

lock_button = tk.Button(root, text="Lock Word", command=lock_word)
lock_button.pack(pady=10)

root.mainloop()

# ------------------ Game Starts Here ------------------

if _locked_word:
    print("\n🕵️  Starting 20 Questions Game...")
    print("The system will now ask up to 20 questions to guess the secret word.")
    print("It can make up to 3 guesses. Answer 'yes' or 'no' to each question.")

    questions_asked = 0
    guesses_made = 0
    max_questions = 20
    max_guesses = 3

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

    import random

    while questions_asked < max_questions:
        if questions_asked < len(sample_questions):
            question = sample_questions[questions_asked]
        else:
            question = f"Custom question {questions_asked + 1}: is it helpful?"

        print(f"\nQuestion {questions_asked + 1}: {question}")
        response = input("Your answer (yes/no): ").strip().lower()

        while response not in ['yes', 'no']:
            response = input("Please answer with 'yes' or 'no': ").strip().lower()

        questions_asked += 1

        # Ask if allowed to guess
        if guesses_made < max_guesses:
            guess_permission = input("\nWould you allow the system to guess the word now? (yes/no): ").strip().lower()
            if guess_permission == 'yes':
                guess = input("System guesses: Is your word... ").strip().lower()
                guesses_made += 1
                if guess == _locked_word:
                    print("\n🎉 The system guessed your word correctly!")
                    break
                else:
                    print("❌ Incorrect guess.")

    else:
        print("\n❗ 20 questions reached. The system failed to guess the word.")
        print("🔒 The secret word was:", _locked_word)

# pip install pyenchant - for dictionary validation