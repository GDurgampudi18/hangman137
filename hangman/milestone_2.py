import random

word_list = ['mango', 'papaya', 'orange', 'sharon', 'banana']
print(word_list)
word = random.choice(word_list)
print(word)
guess = input('Enter a single letter')
if len(guess) == 1 & guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")