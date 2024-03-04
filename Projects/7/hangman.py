
# Name of the dictionary file.
# Change to dictionary.txt for full version of the game.
DICTIONARY_FILE = "smallDictionary.txt"
# DICTIONARY_FILE = "dictionary.txt"

# Used to tell runner.py if it should output debugging information.
DEBUG = True

class Hangman:
    """
    Manages the details of Evil Hangman. This class keeps
    tracks of the possible words from a dictionary during
    rounds of hangman, based on guesses so far.
    """

    def __init__(self, words, debug=True):
        """
        Create a new Hangman from the provided set of words and phrases.
        :param words: A set with the words for this instance of Hangman.
        :param debugOn: True if we should print out debugging to terminal.
        """
        self.__difficulty = None
        self.__dict = [word for word in words]
        self.__player_guesses = []

    def num_words(self, length):
        # """
        # Get the number of words in this Hangman of the given length.
        # :param length: The given length to check.
        # :return: the number of words in the original Dictionary
        # with the given length
        # """
        num_words = 0
        for word in DICTIONARY_FILE:
            if len(word) == length:
                num_words += 1
        return num_words

    def prep_for_round(self, word_len, num_guesses, diff):
        # """
        # Get for a new round of Hangman.
        # :param word_len: the length of the word to pick this time.
        # :param num_guesses: the number of wrong guesses before the
        #                     player loses the round.
        # :param diff: The difficulty for this round.
        # """
        for word in self.__dict:
            if len(word) != word_len:
                self.__dict.remove(word)
        self.__num_guesses = num_guesses
        self.__pattern_list = ["-"]*word_len
        self.__difficulty = diff.lower()

    def num_words_current(self):
        """
        The number of words still possible (active) based on the guesses so far.
        :return: the number of words that are still possibilities based on the
        original dictionary and the guesses so far.
        """
        # temp_dict = self.__dict[:]
        # for word in temp_dict:
        #     for letter in range(len(word)):
        #         if letter != ________ and letter != "-"


        return 0

    def get_guesses_left(self):
        # """
        # Get the number of wrong guesses the user has left in
        # this round (game) of Hangman.
        # :return: the number of wrong guesses the user has left
        #          in this round (game) of Hangman.
        # """
        return self.__num_guesses

    def get_guesses_made(self):
        # """
        # Return a string that contains the letters the user has guessed
        # so far during this round.
        # :return: a string that contains the letters the user
        #          has guessed so far during this round.
        # """
        return " ".join(letter for letter in self.__player_guesses)

    def already_guessed(self, guess):
        # """
        # Check the status of a character.
        # :param guess: The character to check.
        # :return: true if guess has been used or guessed this round of Hangman,
        #          false otherwise.
        # """
        return guess in self.__player_guesses

    def get_pattern(self):
        # """
        # Get the current pattern. The pattern contains '-''s for
        # unrevealed (or guessed) characters and the actual character
        # for "correctly guessed" characters.
        # :return: the current pattern.
        # """
        return "".join(letter for letter in self.__pattern_list)

    def make_guess(self, guess):
        """
        Update the game status (pattern, wrong guesses, word list),
        based on the given guess.
        :param guess: the current guessed character
        :return: a dict with the resulting patterns and the number of
        words in each of the new patterns.
        The return value is for testing and debugging purposes.
        """
        if DEBUG:
            self.debugging(guess)
        return None

    def get_map_pattern(self, guess):
        """
        Precondition: guess has not been guessed before in this round.
        Postcondition: Returns a dictionary that maps patterns to a list of words that 
                       follow said pattern.
        
        :param guess: The current guessed character.
        :return: A dictionary that maps patterns to a list of words that follow said pattern.
        """
        if self.already_guessed(guess):
            raise ValueError("Already guessed")
        return None

    def make_dash_pattern(self, word, guess):
        """
        Precondition: guess has not been guessed before in this round, word is not None.
        Postcondition: Builds possible word patterns for each word based on the user's guess and 
                       the previous pattern.
        
        :param word: The word to build the pattern for.
        :param guess: The current guessed character.
        :return: The dash pattern for the given word based on the user's guess and the previous 
                 dash pattern.
        """
        if self.already_guessed(guess):
            raise ValueError("Already guessed")
        possible_patterns = 

        return ""

    def sort(self, entries):
        '''
        Precondition: entries must be a list of tuples 
        (size word list, dash count, pattern, word list)
        Postcondition: return sorted list of entries - first sort by number of words in word list,
        then the dash amount in the pattern, next the lexicographic ordering for the pattern,
        and finally the word list itself
        :returns: a new sorted list.
        '''
        return None

    def order_entries(self, word_family):
        """
        Precondition: word_family is not None.
        Postcondition: For each key-value pair of (pattern, word list) in word_family, an Entry 
        tuple (size word list, dash count, pattern, word list) is created and added to a list. 
        The entry list is then sorted based on the size of each word list, the number
        of characters revealed in the pattern, and the lexicographical ordering of the patterns.
        
        :param word_family: A dictionary containing patterns as keys and lists of words as values.
        :return: A sorted list of Entry tuples (size word list, dash count, pattern, word list).
        """
        return None

    def get_diff(self, entries):
        """
        Precondition: entries is not None.
        Postcondition: Returns an integer that describes the state of the selection process 
        of word list based on a player's turn and game difficulty.
        Returns a 2 if the AI CAN pick the 2nd hardest word list. For easy mode, it's
        every other valid guess. For medium, it's every 4th valid guess.
        Returns 1 if the AI SHOULD pick the 2nd hardest word list on easy/medium mode,
        but entries.size() <= 1, so it picks the hardest.
        Returns 0 if the AI is picking the hardest list.
        
        :param entries: A list of tuples () representing patterns and associated word lists.
        :return: An integer representing the state of the selection process.
        """
        if not entries:
            raise ValueError("Entries can't be None")
        medium_guess = 4
        easy_mode = "easy"
        medium_mode = "medium"
        if ((self.__difficulty == medium_mode and len(self.__player_guesses) % medium_guess == 0) or
            (self.__difficulty == easy_mode and len(self.__player_guesses) % 2 == 0)):
            if len(entries) > 1:
                return 2
            return 1
        return 0

    def get_difficulty(self, entries):
        """
        Precondition: entries is not None.
        Postcondition: Returns the index of the Entry tuple from the list that the AI 
        will choose for its word list/family depending on the state of the selection process.
        
        :param entries: A list of Entry tuples representing patterns and associated word lists.
        :return: The index of the Entry tuple that the AI will choose.
        """
        if not entries:
            raise ValueError("Entries can't be None")
        diff = self.get_diff(entries)
        if diff == 2:
            return 1
        return 0

    def get_secret_word(self):
        """
        Return the secret word this Hangman finally ended up picking for this round.
        If there are multiple possible words left, one is selected at random.
        The seed should be initialized to 0 before picking.
        :return: return the secret word the manager picked.
        """
        return ""

    def debugging(self, entries):
        """
        Precondition: entries is not None.
        Postcondition: Prints out custom debugging messages about which word family 
        and pattern is chosen depending on difficulty and player's turn.
        """
        sb = []
        diff = self.get_diff(entries)
        sb.append("DEBUGGING: ")
        if diff == 2:
            sb.append("Difficulty second hardest pattern and list.\n\n")
        elif diff == 1:
            sb.append("Should pick second hardest pattern this turn, "
                    + "but only one pattern available.\n")
            sb.append("\nDEBUGGING: Picking hardest list.\n")
        else:
            sb.append("Picking hardest list.\n")

        sb.append("DEBUGGING: New pattern is: ")
        sb.append(self.get_pattern())
        sb.append(". New family has ")
        sb.append(str(self.num_words_current()))
        sb.append(" words.")
        print(''.join(sb))
