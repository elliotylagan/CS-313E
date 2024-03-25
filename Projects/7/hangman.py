# Name 1: Ryan Schlimme
# EID 1: rjs4499

# Name 2: Elliot Ylagan
# EID 2:EPY82

'''
Implementing a mean version of hangman where the computer waits as long as possible
to make a choice
'''

import random

# Name of the dictionary file.
# Change to dictionary.txt for full version of the game.
#DICTIONARY_FILE = "smallDictionary.txt"
DICTIONARY_FILE = "smallDictionary.txt"

# Used to tell runner.py if it should output debugging information.
DEBUG = True


class Hangman:
    """
    Manages the details of Evil Hangman. This class keeps
    tracks of the possible words from a dictionary during
    rounds of hangman, based on guesses so far.
    """

    def __init__(self, words, debug=DEBUG):
        """
        Create a new Hangman from the provided set of words and phrases.
        :param words: A set with the words for this instance of Hangman.
        :param debugOn: True if we should print out debugging to terminal.
        """
        self.__words = words
        self.__debug = debug
        self.__counter = 0
        if self.__words == set() or self.__words is None:
            raise ValueError("Set of words must not be empty.")
        self.__difficulty = None
        self.__player_guesses = []

    def num_words(self, length):
        """
        Get the number of words in this Hangman of the given length.
        :param length: The given length to check.
        :return: the number of words in the original Dictionary
        with the given length
        """
        answer = 0
        for word in self.__words:
            if len(word) == length:
                answer += 1
        return answer

    def prep_for_round(self, word_len, num_guesses, diff):
        """
        Get for a new round of Hangman.
        :param word_len: the length of the word to pick this time.
        :param num_guesses: the number of wrong guesses before the
                            player loses the round.
        :param diff: The difficulty for this round.
        """
        self.__num_guesses = num_guesses
        self.__word_len = word_len
        self.__difficulty = diff.lower()
        self.__pattern = "-"*self.__word_len
        self.__allowed_words = set()
        for i in self.__words:
            if len(i) == self.__word_len:
                self.__allowed_words.add(i)
        self.__player_guesses = []
        # if self.__num_guesses < 1:
        #     raise ValueError("Number of guesses must be at least 1")
        # if not isinstance(self.__num_guesses, int):
        #     raise TypeError("Number of guesses must be an integer")
        # if self.__word_len <= 0:
        #     raise ValueError("Word length must be greater than 0")
        # if self.__difficulty not in ["hard", "easy", "medium"]:
        #     raise ValueError("Difficulty must be EASY, MEDIUM, or HARD")

    def num_words_current(self):
        """
        The number of words still possible (active) based on the guesses so far.
        :return: the number of words that are still possibilities based on the
        original dictionary and the guesses so far.
        """
        return len(self.__allowed_words)

    def get_guesses_left(self):
        """
        Get the number of wrong guesses the user has left in
        this round (game) of Hangman.
        :return: the number of wrong guesses the user has left
                 in this round (game) of Hangman.
        """
        return self.__num_guesses - len(self.__player_guesses) + self.__counter

    def get_guesses_made(self):
        """
        Return a string that contains the letters the user has guessed
        so far during this round.
        :return: a string that contains the letters the user
                 has guessed so far during this round.
        """
        self.__player_guesses.sort()
        return self.__player_guesses

    def already_guessed(self, guess):
        """
        Check the status of a character.
        :param guess: The character to check.
        :return: true if guess has been used or guessed this round of Hangman,
                 false otherwise.
        """
        return guess in self.__player_guesses

    def get_pattern(self):
        """
        Get the current pattern. The pattern contains '-''s for
        unrevealed (or guessed) characters and the actual character
        for "correctly guessed" characters.
        :return: the current pattern.
        """
        return self.__pattern

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
        if guess in self.__player_guesses:
            return "You already guessed that! Pick a new letter please."
        if not isinstance(guess, str) or len(guess) != 1:
            return "That is not an English letter."
        self.__player_guesses.append(str(guess))

        family = self.get_map_pattern(guess)

        family = self.order_entries(family)

        index = self.get_difficulty(family)

        try:
            answer = family[index]
        except IndexError:
            answer = family[-1]

        if self.__pattern != answer[2]:
            self.__counter += 1
            self.__pattern = answer[2]

        self.__pattern = answer[2]

        self.__allowed_words = answer[3]

        # if len(answer[-1]) == 1:
        #     replace = self.__pattern.replace("-", guess)
        #     if replace == answer[0]:
        #         self.__player_guesses = []
        #         self.__counter = 0

        # if self.get_guesses_left() == 0:
        #     self.__player_guesses = []
        #     self.__counter = 0

        return answer

    def get_map_pattern(self, guess):
        """
        Precondition: guess has not been guessed before in this round.
        Postcondition: Returns a dictionary that maps patterns to a list of words that 
                       follow said pattern.

        :param guess: The current guessed character.
        :return: A dictionary that maps patterns to a list of words that follow said pattern.
        """

        pattern = self.get_pattern()
        indices = [index for index, chr in enumerate(pattern) if chr == "-"]
        pattern = list(pattern)
        null = ""
        for i in range(4):
            if i in indices:
                null += "0"

        # Create a dictionary of all possible patterns
        null = "0"*self.__word_len
        inter = ["1" * len(null)]
        while null != "1"*self.__word_len:
            inter.append(null)
            null = str(bin(int(null, 2) + int("1", 2)))[2:]
            null = null.rjust(len(inter[0]), "0")
        for i in range(len(inter)):
            word = inter[i]
            new_word = []
            index = 0
            for j in range(len(pattern)):
                if pattern[j] == "-":
                    if word[index] == "0":
                        new_word.append("-")
                        index += 1
                    else:
                        new_word.append(guess)
                        index += 1
                else:
                    new_word.append(pattern[j])
            inter[i] = "".join(new_word)
        answer = {}
        for i in inter:
            answer[i] = []

        # Patterns and words list for each pattern
        for key, value in answer.items():
            if guess not in key:
                for word in self.__allowed_words:
                    if guess not in word:
                        value.append(word)
                answer[key] = value[:]
                continue
            indices = [index for index, chr in enumerate(key) if chr == guess]
            # print(key, indices)
            for word in self.__allowed_words:
                test = []
                for j in indices:
                    if word[j] == guess:
                        test.append(True)
                    else:
                        test.append(False)
                for j in range(self.__word_len):
                    if j in indices:
                        continue
                    if word[j] == guess:
                        test.append(False)
                if all(test):
                    value.append(word)
            answer[key] = value[:]

        for key in list(answer):
            if answer[key] == []:
                del answer[key]

        return answer

    # def make_dash_pattern(self, word, guess):
    #     """
    #     Precondition: guess has not been guessed before in this round, word is not None.
    #     Postcondition: Builds possible word patterns for each word based on the user's guess and
    #                    the previous pattern.

    #     :param word: The word to build the pattern for.
    #     :param guess: The current guessed character.
    #     :return: The dash pattern for the given word based on the user's guess and the previous
    #              dash pattern.
    #     """
    #     return ""
    # Implemented in previous logic!!!!!!!!!!!

    def merge(self, nums1, nums2):
        '''
        Implements the merge for merge sort (helper function)
        '''
        answer = []
        i = j = 0
        while len(answer) < len(nums1) + len(nums2):
            # if index == 3:
            #     a = len(nums1[i][3])
            #     b = len(nums2[j][3])
            # else:
            #     a = nums1[i][index]
            #     b = nums2[j][index]
            if i == len(nums1):
                answer.append(nums2[j])
                j += 1
            elif j == len(nums2):
                answer.append(nums1[i])
                i += 1
            elif nums1[i] < nums2[j]:
                answer.append(nums1[i])
                i += 1
            else:
                answer.append(nums2[j])
                j += 1
        return answer

    def merge_sort(self, nums):
        '''
        Performs the merge sort
        '''
        if len(nums) <= 1:
            return nums
        return self.merge(self.merge_sort(nums[:len(nums)//2]),
                          self.merge_sort(nums[len(nums)//2:]))

    def sort(self, entries):
        '''
        Precondition: entries must be a list of tuples 
        (size word list, dash count, pattern, word list)
        Postcondition: return sorted list of entries - first sort by number of words in word list,
        then the dash amount in the pattern, next the lexicographic ordering for the pattern,
        and finally the word list itself
        :returns: a new sorted list.
        '''

        entries = self.merge_sort(entries)

        return entries

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
        family_list = []

        for key in word_family:
            word_list = word_family[key]
            length = len(word_list)
            pattern = key
            dashes = key.count("-")
            family_list.append((length, dashes, pattern, word_list))

        family_list = self.sort(family_list)

        return family_list

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
            return -2
        return -1

    def get_secret_word(self):
        """
        Return the secret word this Hangman finally ended up picking for this round.
        If there are multiple possible words left, one is selected at random.
        The seed should be initialized to 0 before picking.
        :return: return the secret word the manager picked.
        """
        self.__allowed_words = list(self.__allowed_words)
        if len(self.__allowed_words) == 1:
            return self.__allowed_words[0]
        random.seed(0)
        index = random.randint(0, len(self.__allowed_words)-1)
        answer = self.__allowed_words[index]
        return answer

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
