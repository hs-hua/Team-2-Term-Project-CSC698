import tkinter as tk
import random
from tkinter import messagebox

class GuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number Game")


        self.score = 0

        # Widgets


        self.entry = tk.Entry(root)
        self.entry.pack(pady=5)


        self.play_button = tk.Button(root, text="Play", command=self.generate, command=self.play_game)
        self.play_button.pack(pady=10)

        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(root, text="Score: 0", font=("Arial", 12, "bold"))
        self.score_label.pack(pady=5)

    def play_game(self):

        global generated_number
        num1 = random.randint(0, 10)
        num2 = random.randint(0, 10)

        #try a function that has a predictable number to test the scoring mechanism
        operation = random.choice(['+','-','*','/'])
        if operation == '+':
            generated_number = num1 + num2
            self.result_label.config(
                text=f"{num1} + {num2} = ")

        if operation == '-':
            generated_number = num1 - num2
            self.result_label.config(
                text=f"{num1} - {num2} = ")
        if operation == '*':
            generated_number = num1 * num2
            self.result_label.config(
                text=f"{num1} * {num2} = ")
        elif operation == '/':
            while num2 == 0:
                num2 = random.randint(1,10)
            generated_number = round(num1/num2, 2)
            self.result_label.config(
                text=f"{num1} / {num2} = ")

        user_input = self.entry.get()

        # Validate input
        if not user_input.isdigit() or not (0 <= int(user_input) <= 10):
            messagebox.showerror("Invalid input", "Please enter an integer between 0 and 10.")
            return

        user_guess = int(user_input)
        #generated_number = random.randint(0, 10)
        if user_guess == generated_number:
            self.score += 1
            result_text = "🎉 You guessed it right!"
        else:
            result_text = "❌ Try again!"

        self.result_label.config(
            text=f"{result_text}\nYour Guess: {user_guess}\nGenerated Number: {generated_number}\nWould you like to play again? Please enter the number."
        )
        self.score_label.config(text=f"Score: {self.score}")

        # Clear input field for next round
        self.entry.delete(0, tk.END)

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()