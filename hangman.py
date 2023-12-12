'''
Stuart Elliott Hangman project [AI Core]

Make sure you complete all the TODOs in this file.
The prints have to contain the same text as indicated, don't add any more prints,
or you will get 0 for this assignment.
'''
import random


class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
        
    '''
    
    def __init__(self, word_list, num_lives=5):
        """
        The function initializes an object with a word list and a number of lives.
        
        :param word_list: The word_list parameter is a list of words that will be used in the game.
        These words will be randomly selected for the player to guess
        :param num_lives: The number of lives or chances a player has in a game. It determines how many
        incorrect guesses the player can make before losing the game. The default value is 5, but it can
        be customized by passing a different value when creating an instance of the class, defaults to 5
        (optional)
        """
        # TODO 2: Initialize the attributes as indicated in the docstring
        self.word = random.choice(word_list)
        self.word_guessed = list('_' * len(self.word))
        self.num_letters = len(set(list(self.word)))
        self.num_lives = num_lives
        self.list_letters = []
        self.drawn_hangman = [
            '''
              ________
              |/     |     
              |      O/     
              |     /|
              |     / |
            __|____
            ''',''' 
              ________
              |/     |
              |      O 
              |      |
              |     / |
            __|____
            ''',''' 
              ________
              |/     |
              |      O 
              |      |
              |     / 
            __|____
            ''',''' 
              ________
              |/     |
              |      O 
              |      |
              |      
            __|____
            ''',''' 
              ________
              |/     |
              |      O 
              |      
              | 
            __|____
            ''']
        # TODO 2: Print two message upon initialization:
        # 1. "The mystery word has {len(self.word)} characters" (The number of letters is NOT the UNIQUE number of letters)
        # 2. {word_guessed}
       
       
        print(f"The mystery word has {self.num_letters} characters")
        print(f"{self.word_guessed}")

    def check_guess(self, letter) -> None:
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''
        # TODO 3: Check if the letter is in the word. TIP: You can use the lower() method to convert the letter to lowercase
        letter = letter.lower()
        if letter in self.word:
            print(f"The letter {letter} is in the word!")
        # TODO 3: If the letter is in the word, replace the '_' in the word_guessed list with the letter
            letter_index = 0
            for position, let in enumerate(self.word):
                if let == letter:
                    letter_index = position
                    self.word_guessed[letter_index] = letter
            print(f"{letter} is in the word!")
            print(f"{self.word_guessed}")
        # TODO 3: If the letter is in the word, the number of UNIQUE letters in the word that have not been guessed yet has to be reduced by 1
            self.num_letters -= 1
        # TODO 3: If the letter is not in the word, reduce the number of lives by 1
        else:
            self.num_lives -= 1
            print(f"Sorry, {letter} is not in the word.")
            print(f"{self.drawn_hangman[self.num_lives]}")
            print(f"You have {self.num_lives} lives left.")
        # appends letter to list_letters
        self.list_letters.append(letter)
        # Be careful! A letter can contain the same letter more than once. TIP: Take a look at the index() method in the string class

    def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        # TODO 1: Ask the user for a letter iteratively until the user enters a valid letter
        # TODO 1: Assign the letter to a variable called `letter`
        # TODO 1: The letter has to comply with the following criteria: It has to be a single character. If it is not, print "Please, enter just one character"
        letter = input("Please enter a letter: ")
        if len(letter) != 1:
            print("Please, enter just one character")
        # TODO 2. It has to be a letter that has not been tried yet. Use the list_letters attribute to check this. If it has been tried, print "{letter} was already tried".
        elif letter in self.list_letters:
            print(f"{letter} was already tried")
        # TODO 3: If the letter is valid, call the check_letter method
        else:
            self.check_guess(letter)
            

def play_game(word_list):
    """
    The function "play_game" takes a word list as input and passes it to check_guess.
    
    :param word_list: A list of words that will be used in the game
    
    The `word_list` variable is a list of words that will be used in the Hangman game. These words
    will be randomly selected for the player to guess.
    
    """
    # As an aid, part of the code is already provided:
    game = Hangman(word_list, num_lives=5)
    # TODO 1: To test this task, you can call the ask_letter method
    # game.ask_letter()
    # TODO 2: To test this task, upon initialization, two messages should be printed
    # game.__init__(word_list)
    # TODO 3: To test this task, you call the ask_letter method and check if the letter is in the word
    # game.check_letter()
    # TODO 4: Iteratively ask the user for a letter until the user guesses the word or runs out of lives
    # If the user guesses the word, print "Congratulations, you won!"
    # If the user runs out of lives, print "You ran out of lives. The word was {word}"
    while True:
        if game.num_lives == 0:
            print(f"You lost! The word was {game.word}")
            break
        elif game.num_letters > 0:
            game.ask_letter()
        else:
            print("Congratulations! You won!")
            break

if __name__ == '__main__':
    word_list = ['raspberry', 'banana', 'fig', 'jackfruit', 'watermelon']
    play_game(word_list)
# %%