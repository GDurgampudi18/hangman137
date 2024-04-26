import random

word_list = ['mango', 'papaya', 'orange', 'sharon', 'banana']
print(word_list)
word = random.choice(word_list)
print(word)
def check_guess(guess):
    guess.lower()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
    
def ask_for_input():
    while True:
        guess = input('Enter a single letter: ')
        if len(guess) != 1 or guess.isalpha() == False:               
            print('Invalid letter. Please, enter a single alphabetical character.')
            continue
        check_guess(guess)
ask_for_input()


 