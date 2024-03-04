"""Runner File. You do not need to modify this"""
import os
from hangman import Hangman, DEBUG, DICTIONARY_FILE

difficulty_dict = {
    1: "EASY",
    2: "MEDIUM",
    3: "HARD"
}

MAX_GUESSES = 25

class Runner:

    """
    Class Runner is the driver program for the Hangman program. It reads 
    a dictionary of words to be used during the game and then plays a game with
    the user.

    This is a cheating version of hangman that delays picking a word
    to keep its options open. You can change the setting for DEBUG to see
    how many options are still left on each turn and what patterns are
    being generated from the guess.

    Based on a program by Stuart Reges, modified by Mike Scott and Jesse Zou.
    """

    @staticmethod
    def main():
        """
        main method
        """
        # Run the game with a human user.
        print("Welcome to the CS313E hangman game.")
        print()

        # read in the dictionary and create the Hangman manager
        dictionary = Runner.get_dictionary()
        hangman = Hangman(dictionary)
        if DEBUG:
            Runner.show_word_counts(hangman)

        # play games until user wants to quit
        while True:
            Runner.set_game_parameters(hangman)
            Runner.play_game(hangman)
            Runner.show_results(hangman)

            # play games until user wants to quit
            if not Runner.play_again():
                break

    @staticmethod
    def play_again():
        """
        Check to see if the user wants to play another game.

        Parameters:
            keyboard: We assume the input is connected to standard input.

        Returns:
            True if the user wants to play another game, False otherwise.
        """

        print()
        answer = input("Another game? Enter y for another game, "
                       "anything else to quit: ")
        return len(answer) > 0 and answer.lower().startswith('y')

    @staticmethod
    def set_game_parameters(hangman):
        """
        Get user choices for the current game of Hangman.

        Preconditions:
            - hangman is not None and initialized with correct dictionary.
            - keyboard is connected to standard input.
        """

        if not hangman:
            raise ValueError("hangman manager may not be null")

        while True:
            try:
                word_length = int(input("What length word do you want to use? "))
                if Runner.at_least_one_word(hangman, word_length):
                    break
            except ValueError:
                print("Error: Please enter a valid integer for word length.")

        while True:
            try:
                num_guesses = int(input("How many wrong answers allowed? "))
                if Runner.valid_choice(num_guesses, 1, MAX_GUESSES, "number of wrong guesses"):
                    break
            except ValueError:
                print("Error: Please enter a valid integer for number of wrong guesses.")

        difficulty = Runner.get_difficulty()
        hangman.prep_for_round(word_length, num_guesses, difficulty)

    @staticmethod
    def get_difficulty():
        """
        Determine difficulty level from the user. They must enter a valid choice.

        Parameters:
            keyboard: The input source (not None).

        Preconditions:
            - keyboard is not None.
        """

        while True:
            try:
                print("What difficulty level do you want?")
                diff_choice = int(input(f"Enter a number between {1} (EASIEST) and {3} (HARDEST): "))
                if Runner.valid_choice(diff_choice, 1, 3, "difficulty"):
                    break
            except ValueError:
                print("Error: Please enter a valid integer for difficulty level.")
        return difficulty_dict[diff_choice]

    @staticmethod
    def valid_choice(choice, min_val, max_val, explanation):
        '''
        Determine if choice is within the range [min, max]
        '''
        valid = min_val <= choice <= max_val
        if not valid:
            print(f"{choice} is not a valid number for {explanation}")
            print(f"Pick a number between {min_val} and {max_val}.")
        return valid

    @staticmethod
    def at_least_one_word(hangman, word_length):
        '''
        check to ensure there is at least one word of 
        the given length in the manager
        '''
        num_words = hangman.num_words(word_length)
        if num_words == 0:
            print()
            print(f"I don't know any words with {word_length} letters. Enter another number.")
        return num_words != 0

    @staticmethod
    def get_dictionary():
        """
        Open the dictionary file and return a list containing the words in the dictionary file.

        Returns:
            A list containing the words in the dictionary file.

        Raises:
            FileNotFoundError: If the dictionary file is not found, the program ends.
        """

        dictionary = set()
        try:
            with open(DICTIONARY_FILE, 'r') as f:
                for word in f:
                    dictionary.add(word.strip().lower())
        except FileNotFoundError:
            print(f"Unable to find this file: {DICTIONARY_FILE}")
            print("Program running in this directory: ", os.getcwd())
            print("Be sure the dictionary file is in that directory")
            print("Returning empty list for dictionary.")
        return sorted(set(dictionary))

    @staticmethod
    def play_game(hangman):
        '''
        Plays one game with the user
        '''

        # keep asking for guesses as long as 
        # user has guesses left and puzzle not solved the puzzle
        while hangman.get_guesses_left() > 0 and '-' in hangman.get_pattern():
            print("Guesses left:", hangman.get_guesses_left())

            # debugging
            if DEBUG:
                print("DEBUGGING: Words left:", hangman.num_words_current())

            print("Guessed so far:", hangman.get_guesses_made())
            print("Current word:", hangman.get_pattern())
            print()
            guess = Runner.get_letter(hangman)
            results = hangman.make_guess(guess)
            if DEBUG:
                Runner.show_patterns(results)
            Runner.show_result_of_guess(hangman, guess)

    @staticmethod
    def show_result_of_guess(hangman, guess):
        '''
        shows the result of the user guess
        '''
        if not hangman.get_pattern():
            raise ValueError("Pattern may not be None")

        count = hangman.get_pattern().count(guess)
        if count == 0:
            print(f"Sorry, there are no {guess}'s")
        elif count == 1:
            print(f"Yes, there is one {guess}")
        else:
            print(f"Yes, there are {count} {guess}'s")

    @staticmethod
    def get_letter(manager):
        """
        precondition: manager != None
        """
        if not manager:
            raise ValueError("manager may not be None")
        already_guessed = True
        while already_guessed:
            result = input("Your guess? ").lower()
            while not result or not result[0].isalpha() or len(result) > 1:
                print("That is not an English letter.")
                result = input("Your guess? ").lower()
            guess = result[0]
            already_guessed = manager.already_guessed(guess)
            if already_guessed:
                print("You already guessed that! Pick a new letter please.")
        assert guess.isalpha() and not manager.already_guessed(guess), f"something wrong with my logic in getting guess. {guess}"
        return guess

    @staticmethod
    def show_patterns(results):
        """
        Debugging method to show current patterns and number of words for each.

        Parameters:
            results (dict): A dictionary containing patterns as keys and the number of words for each pattern as values.

        Preconditions:
            results is not None.
        """
        if not results:
            raise ValueError("results may not be none")
        print("DEBUGGING: Based on guess here are the resulting patterns and")
        print("number of words in each pattern:")
        for key, value in results.items():
            print(f"Pattern: {key}, Number of words: {value}")
        print("END DEBUGGING")
        print()

    @staticmethod
    def show_results(hangman):
        '''
        reports the results of the game, including showing the answer
        '''

        # if the game is over, get the secret word
        answer = hangman.get_secret_word()
        print("Answer =", answer)
        if hangman.get_guesses_left() > 0:
            print("You beat me")
        else:
            print("Sorry, you lose")

    @staticmethod
    def show_word_counts(hangman):
        """
        Helper method for debugging. Display the number of words of each length in the dictionary.

        The dictionary file contains words of lengths ranging from 2 to 25.
        """

        MAX_LETTERS_PER_WORD = 25
        print("Number of words of each length in the dictionary:")
        for i in range(2, MAX_LETTERS_PER_WORD):
            print(f"{i}: {hangman.num_words(i)}")

if __name__ == "__main__":
    Runner.main()
