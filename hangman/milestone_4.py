import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)       
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.list_of_guesses = []

        print(f"The mystery word has {len(self.word)} characters")
        print(f"{self.word_guessed}")

    def check_guess(self, guess):
        guess.lower()
        ran_word = self.word
        if guess in ran_word:
            print(f"Good guess! {guess} is in the word.")
            for let in ran_word:
                if let == guess:
                    ind_g = ran_word.index(guess)
                    self.word_guessed[ind_g] = guess
            self.num_letters -= 1
        else:
            self.num_lives -= 1
            print(f'Sorry, {guess} is not in the word.')
            print(f'You have {self.num_lives} lives left.')

    def ask_for_input(self):
        while True:
            guess = input('Enter a single letter: ')
            if len(guess) != 1 or guess.isalpha() == False:               
                print('Invalid letter. Please, enter a single alphabetical character.')
                continue
            elif guess in self.list_of_guesses:
                print(f"You already tried that letter!")
                continue
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(str.lower(guess))
                break
word_list = ['apple', 'banana', 'mango', 'guava', 'coconut']
hang = Hangman(word_list, num_lives=5)
hang.ask_for_input()
                   

