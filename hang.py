import random
import string
import logging


def testAsserts(param,typeParam,msgNone,msgType):
    assert param !=None,msgNone 
    assert type(param)!=typeParam,msgType 


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
    testAsserts(lettersGuessed,string,"lettersGuessed receiving null","lettersGuessed not a String")
    testAsserts(secretWord,string,"secretWord receiving null","secretWord not a String")
    
    for letter in secretWord:
        if letter in lettersGuessed:
            pass
        else:
            return False
    return True


def isLetterGuessed(letter, lettersGuessed):
    testAsserts(lettersGuessed,string,"lettersGuessed receiving null","lettersGuessed not a String")
    testAsserts(letter,string,"lettersGuessed receiving null","lettersGuessed not a String")

    guessed = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            guessed += letter
        else:
            guessed += '_ '
    return guessed


def hangman(secretWord):

    logging.basicConfig(filename='hangmanlog.log',level=logging.DEBUG)
    testAsserts(secretWord,string,"secretWord receiving null","secretWord not a String")
    
    guesses = 8
    lettersGuessed = []
    print('Welcome to the game, Hangam!')
    print('I am thinking of a word that is', len(secretWord), ' letters long.')
    print('-------------')
    
    logging.debug("start - isWordGuessed()")

    while  isWordGuessed(secretWord, lettersGuessed) == False and guesses >0:
        print('You have ', guesses, 'guesses left.')

        available = string.ascii_lowercase
        for letter in available:
            if letter in lettersGuessed:
                available = available.replace(letter, '')

        print('Available letters', available)
        
        logging.debug("letter input")
        
        letter = input('Please guess a letter: ')
        
        
        
        if letter in lettersGuessed:

            guessed = isLetterGuessed(letter, lettersGuessed)
            
            logging.debug("already guessed that letter")
            
            print('Oops! You have already guessed that letter: ', guessed)
            
            
        elif letter in secretWord:
            lettersGuessed.append(letter)

            guessed = isLetterGuessed(letter, lettersGuessed)
            
            logging.debug("good guess")
            
            print('Good Guess: ', guessed)
            
        else:
            guesses -=1
            lettersGuessed.append(letter)

            guessed = isLetterGuessed(letter, lettersGuessed)
            
            logging.debug("letter not in my word")
            
            print('Oops! That letter is not in my word: ',  guessed)
        print('------------')

    else:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            logging.debug("Victory")
            print('Congratulations, you won!')
        else:
            logging.debug("Defeat")
            print('Sorry, you ran out of guesses. The word was ', secretWord, '.')


secretWord = loadWords().lower()
hangman(secretWord)
