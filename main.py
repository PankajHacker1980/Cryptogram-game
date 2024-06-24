import random

class Cryptogram:
    def __init__(self):
        self.words = [
            "python", "programming", "algorithm", "cryptogram", "challenge",
            "word", "puzzle", "code", "solution", "game", "fun", "learning"
        ]
        self.secret_word = random.choice(self.words).lower()
        self.letter_mapping = self.create_letter_mapping()
    
    def create_letter_mapping(self):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        shuffled_alphabet = list(alphabet)
        random.shuffle(shuffled_alphabet)
        
        letter_mapping = {}
        for original, shuffled in zip(alphabet, shuffled_alphabet):
            letter_mapping[original] = shuffled
        
        return letter_mapping
    
    def encrypt_message(self):
        encrypted_message = ''.join(self.letter_mapping[char] if char in self.letter_mapping else char for char in self.secret_word)
        return encrypted_message
    
    def decrypt_message(self, encrypted_message):
        decrypted_message = ''.join(self.letter_mapping.get(char, char) for char in encrypted_message)
        return decrypted_message
    
    def play_game(self):
        print("Welcome to the Cryptogram Game!")
        print("Try to decipher the secret word.")
        print(f"Encrypted message: {self.encrypt_message()}")

        guess_mapping = {}
        while True:
            guess = input("Enter a letter guess (or 'quit' to exit): ").strip().lower()
            
            if guess == 'quit':
                print("Exiting the game.")
                break
            
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input! Please enter a single letter.")
                continue
            
            if guess in guess_mapping:
                print(f"You've already guessed the mapping for '{guess}'.")
                continue
            
            replacement = input(f"Enter the replacement for '{guess}': ").strip().lower()
            
            if len(replacement) != 1 or not replacement.isalpha():
                print("Invalid input! Please enter a single letter.")
                continue
            
            guess_mapping[guess] = replacement
            print(f"Updated mapping: {guess_mapping}")
            
            decrypted_message = self.decrypt_message(self.secret_word)
            print(f"Decrypted message: {decrypted_message}")
            
            if all(char.isalpha() and char in guess_mapping for char in self.secret_word):
                print(f"\nCongratulations! You deciphered the secret word: {decrypted_message}")
                break

if __name__ == "__main__":
    game = Cryptogram()
    game.play_game()
