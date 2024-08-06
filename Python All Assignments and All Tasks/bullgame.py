import random

def generate_number():
    """Generate a random 4-digit number with unique digits."""
    digits = list(range(10))
    random.shuffle(digits)
    number = ''.join(map(str, digits[:4]))
    return number

def get_cows_and_bulls(guess, number):
    """Calculate cows and bulls based on the guess and the number."""
    cows = sum(g == n for g, n in zip(guess, number))
    bulls = sum(guess.count(n) for n in set(number)) - cows
    return cows, bulls

def cows_and_bulls_game():
    number = generate_number()
    attempts = 0
    
    print("Welcome to the Cows and Bulls Game!")
    
    while True:
        guess = input("Enter a 4-digit number: ")
        
        if len(guess) != 4 or not guess.isdigit():
            print("Please enter a valid 4-digit number.")
            continue
        
        attempts += 1
        cows, bulls = get_cows_and_bulls(guess, number)
        
        if cows == 4:
            print(f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
            break
        
        print(f"{cows} cow(s), {bulls} bull(s)")

if __name__ == "__main__":
    cows_and_bulls_game()






def display_word(word, guessed_letters):
    """Display the current state of the word with guessed letters."""
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def hangman_game():
    word = "EVAPORATE"
    guessed_letters = set()
    
    print("Welcome to Hangman!")
    
    while True:
        print(display_word(word, guessed_letters))
        
        guess = input("Guess a letter: ").upper()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You've guessed the word: {word}")
            break
        
        if guess not in word:
            print("Incorrect!")

if __name__ == "__main__":
    hangman_game()
