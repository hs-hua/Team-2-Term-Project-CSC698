from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch


class TwentyQuestionsAI:
    def __init__(self):
        print("Loading the AI model... this might take a moment.")

        # Load the model and tokenizer from Hugging Face
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        self.model = GPT2LMHeadModel.from_pretrained("gpt2")

        # Fix a technical issue with the tokenizer
        self.tokenizer.pad_token = self.tokenizer.eos_token

        print("AI model loaded successfully!")

        # Game variables
        self.questions_asked = 0
        self.max_questions = 20
        self.category = ""

    def start_game(self):
        print("\n=== Welcome to 20 Questions! ===")
        print("Think of a person, place, or thing.")
        print("I'll try to guess it by asking yes/no questions.")

        # Get the category hint
        self.category = input("\nIs it a person, place, or thing? ").lower().strip()

        print(f"\nOkay! I'll try to guess your {self.category}.")
        print("Please answer my questions with 'yes' or 'no'.\n")

        # Now start asking questions
        self.ask_questions()

    def ask_questions(self):
        while self.questions_asked < self.max_questions:
            # Generate a question using the AI
            question = self.generate_question()
            print(f"Question {self.questions_asked + 1}: {question}")

            # Get player's answer
            answer = input("Your answer: ").lower().strip()

            self.questions_asked += 1

            if answer == "yes":
                print("Interesting!\n")
            elif answer == "no":
                print("I see.\n")

    def generate_question(self):
        # Create a prompt to help the AI generate a good question
        prompt = f"I'm playing 20 questions. I need to guess a {self.category}. "
        prompt += f"Question {self.questions_asked + 1}: Is it"

        # Convert text to numbers the AI understands
        inputs = self.tokenizer.encode(prompt, return_tensors="pt")

        # Generate text using the AI model
        with torch.no_grad():
            outputs = self.model.generate(
                inputs,
                max_length=inputs.shape[1] + 10,
                num_return_sequences=1,
                temperature=0.7,
                do_sample=True,
                pad_token_id=self.tokenizer.eos_token_id
            )

        # Convert the AI's numbers back to text
        generated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Extract just the question part
        question = generated_text.replace(prompt, "").strip()

        # Clean up and make sure it ends with a question mark
        if not question.endswith("?"):
            question += "?"

        return "Is it " + question


# Run the game
if __name__ == "__main__":
    game = TwentyQuestionsAI()
    game.start_game()
