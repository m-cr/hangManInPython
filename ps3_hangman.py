# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for i in lettersGuessed:
        if i in secretWord:
            secretWord = secretWord.replace(i, "")
    if secretWord == '':
        return True
    else:
        return False

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    if secretWord[-1:] == '':
        return ""
    elif secretWord[-1:] in lettersGuessed:
        append = secretWord[-1:]
        return getGuessedWord(secretWord[:-1],lettersGuessed) + append
    elif not(secretWord[-1:] in lettersGuessed):
        append = "_ "
        return getGuessedWord(secretWord[:-1],lettersGuessed) + append



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    left = string.ascii_lowercase
    for i in left:
        if i in lettersGuessed:
            left = left.replace(i,'')
    return left
    

def hangman(secretWord):
    '''
    '''

    #INTRO
    print 'Welcome to the game, Hangman!'
    print 'I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.'
    print '-------------'
    #INTRO
    
    lettersGuessed = ''
    guessLeft = 8
    while isWordGuessed(secretWord, lettersGuessed) == False:
        if guessLeft == 0:
            break
        print 'You have ' + str(guessLeft) + ' guesses left.'
        print 'Available letters: ' + getAvailableLetters(lettersGuessed)
    
        guess = raw_input("Please guess a letter: ")
            
        guessInLower = guess.lower()
            
        if guessInLower in getAvailableLetters(lettersGuessed) and guessInLower in secretWord:
            lettersGuessed += guessInLower
            print 'Good guess: '+getGuessedWord(secretWord, lettersGuessed)
        
        elif guessInLower not in getAvailableLetters(lettersGuessed):
            print 'Oops! You"ve already guessed that letter: ' + getGuessedWord(secretWord, lettersGuessed)
        
        elif guessInLower in getAvailableLetters(lettersGuessed) and guessInLower not in secretWord:
            lettersGuessed += guessInLower
            print 'Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed)
            guessLeft -= 1
    
    if isWordGuessed(secretWord, lettersGuessed) == False:
        print '--------'
        print 'Sorry, you ran out of guesses. The word was else.'
    if isWordGuessed(secretWord, lettersGuessed) == True:
        print '--------'
        print 'Congratulations, you won!'
    
        


    #if isWordGuessed(secretWord, lettersGuessed) == True:
        #return 'Congratulations, you won!'

#print hangman('apple')



# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
