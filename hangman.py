import string
from words import choose_word
from images import IMAGES
'''
Important instruction
* function and variable name snake_case -> is_prime
* contant variable upper case PI
'''

def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return True (if user guess the world correctly )
      return False (wrong selection)
    '''
    count = 0
    for letter in secret_word:
        if (letter in letters_guessed):
            count += 1
    if (count == len(secret_word)):
        return True
    else:
        return False

# if you want to test this function please call function -> get_guessed_word("kindness", [k, n, d])


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: word guess by the user
    letters_guessed: list hold all the word guess by the user
    returns: 
      return string which contain all the right guessed characters
      Example :- 
      if secret_word -> "kindness" and letters_guessed = [k, n, s]
      return "k_n_n_ss"
    '''
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list contains all guessed characters
    returns: 
      it return string which contains all characters except guessed letters
    Example :-
      letters_guessed = ['e', 'a'] then    
      return sting is -> `bcdfghijklmnopqrstuvwxyz`
    '''
    letters_left = string.ascii_lowercase
    for letter in letters_guessed:
        if letters_left.__contains__(letter):
            letters_left = letters_left.replace(letter, '')
    return letters_left

def get_error_image(error_count):
    return IMAGES[error_count]

def ifValid(input_character):
    if((len(input_character) == 1) and (input_character in string.ascii_lowercase)) :
        return True
    else:
        return False

def hangman(secret_word):
    '''
    secret_word (string) : secret word to guessed by the user.

    Steps to start Hangman:

    * In the beginning of the game user will know about the total characters in the secret_word    

    * In each round user will guess one character 

    * After each character give feedback to the user
      * right or wrong

    * Display partial word guessed by the user and use underscore in place of not guess word    
    '''
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(
        str(len(secret_word))), end='\n\n')

    letters_guessed = []
    remaining_lives = 8
    error_count = 0

    if (remaining_lives > 0):
        while (len(letters_guessed) < len(secret_word)):

            print("Remaining lives: {}".format(remaining_lives))

            available_letters = get_available_letters(letters_guessed)
            print("Available letters: {} ".format(available_letters))

            guess = input("Please guess a letter: ")
            letter = guess.lower()

            if (letter == "hint"):
                letters_guessed.append(secret_word[0])
                print("Hint: {} ".format(
                        get_guessed_word(secret_word, letters_guessed)))
                continue

            if(ifValid(letter)):
                if letter in secret_word:
                    letters_guessed.append(letter)
                    print("Good guess: {} ".format(
                        get_guessed_word(secret_word, letters_guessed)))
                    remaining_lives -= 1
                    if is_word_guessed(secret_word, letters_guessed) == True:
                        print(" * * Congratulations, you won! * * ", end='\n\n')
                else:
                    print("Oops! That letter is not in my word: {} ".format(
                        get_guessed_word(secret_word, letters_guessed)))
                    letters_guessed.append(letter)
                    remaining_lives -= 2
                    error_count += 1
                    error_image = get_error_image(error_count)
                    print(error_image)
                    print("")
            else:
                print("Invalid Input!")
    else:
        print("Game Over!")


# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
hangman(secret_word)
