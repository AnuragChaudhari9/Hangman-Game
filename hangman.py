import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses a word from the list
    while '-' in word and ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # track user guessed letters

    lives = 2

    # getting input
    while len(word_letters) > 0 and lives >= 1:
        print("You have", lives, "lives left and you have used these letters:", " ".join(
            used_letters))  # remind user of guessed letters

        word_list = [letter if letter in used_letters else "_" for letter in word]
        print(" ".join(word_list))
        
        user_letter = input("Type your letter: ").upper()
        if user_letter in alphabet - used_letters:
                used_letters.add(user_letter)
                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                else:

                    lives = lives - 1
                    print("letter is not in the word")

        elif user_letter in used_letters:
                print("You have already guessed that letter! Try another letter")

        else:
                print("Invalid input")

    if lives == 0:
        print("You have died! The word was",word)
    else:
        print('Congrats! You guessed the word', word, '!!')


hangman()
