import random
import string



def loadWords():
    wordListFileName = "palavras.txt"
    print("Loading word list from file...")
    # line: string
    line = open(wordListFileName, 'r').readline()
    # wordlist: list of strings
    wordlist = str.split(line)
    print("  ", len(wordlist), "words loaded.")
    return random.choice(wordlist)


def isWordGuessed(secretWord, lettersGuessed):
    for letter in secretWord:
        if letter in lettersGuessed:
            pass
        else:
            return False
    return True


def isLetterGuessed(letter, lettersGuessed):
    guessed = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed += letter
        else:
            guessed += '_ '
    return guessed

def hangman(secretWord):

    guesses = 8
    lettersGuessed = []
    print('Welcome to the game, Hangam!')
    print('I am thinking of a word that is', len(secretWord), ' letters long.')
    print('-------------')

    while  isWordGuessed(secretWord, lettersGuessed) == False and guesses >0:
        print('You have ', guesses, 'guesses left.')

        available = string.ascii_lowercase
        for letter in available:
            if letter in lettersGuessed:
                available = available.replace(letter, '')

        print('Available letters', available)
        letter = input('Please guess a letter: ')
        if letter in lettersGuessed:

            guessed = isLetterGuessed(letter, lettersGuessed)

            print('Oops! You have already guessed that letter: ', guessed)
        elif letter in secretWord:
            lettersGuessed.append(letter)

            guessed = isLetterGuessed(letter, lettersGuessed)

            print('Good Guess: ', guessed)
        else:
            guesses -=1
            lettersGuessed.append(letter)

            guessed = isLetterGuessed(letter, lettersGuessed)

            print('Oops! That letter is not in my word: ',  guessed)
        print('------------')

    else:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print('Congratulations, you won!')
        else:
            print('Sorry, you ran out of guesses. The word was ', secretWord, '.')




secretWord = loadWords().lower()
hangman(secretWord)
