# Name 1: Ryan Schlimme
# EID 1: rjs4499

# Name 2: Elliot Ylagan
# EID 2: EPY82

import sys

# Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise
def is_prime(n):
    if (n == 1):
        return False

    limit = int(n ** 0.5) + 1
    div = 2
    while div < limit:
        if n % div == 0:
            return False
        div += 1
    return True

# Input: takes as input a string in lower case and the size
#        of the hash table 
# Output: returns the index the string will hash into
def hash_word(s, size):
    hash_idx = 0
    for j in range(len(s)):
        letter = ord(s[j]) - 96
        hash_idx = (hash_idx * 26 + letter) % size
    return hash_idx

# Input: takes as input a string in lower case and the constant
#        for double hashing 
# Output: returns the step size for that string 
def step_size(s, const):
    return const - (len(s) % const)

# Input: takes as input a string and a hash table 
# Output: no output; the function enters the string in the hash table, 
#         it resolves collisions by double hashing
def insert_word(s, hash_table):
    index = hash_word(s, len(hash_table))
    const = #lower prime number
    while True:
        if hash_table[index] is not None:
            hash_table[index] = s

        index = (index + step_size(s, const)) % len(hash_table)

# Input: takes as input a string and a hash table 
# Output: returns True if the string is in the hash table 
#         and False otherwise
def find_word(s, hash_table):
    index = hash_word(s, len(hash_table))
    const = #lower prime number

    while hash_table[index] is not None:
        if hash_table[index] == s:
            return True
        index = (index + step_size(s, const)) % len(hash_table)
    return False

# Input: string s, a hash table, and a hash_memo 
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo 
#         and returns True and False otherwise
def is_reducible(s, hash_table, hash_memo): #no clue what to do with hash table
    if s in hash_memo:
        hash_memo.append(s) #change this to hash format, not list format
        return True
    for index in len(s):
        is_reducible(s[:index] + s[index:], hash_table, hash_memo)
    return False

# Input: string_list a list of words
# Output: returns a list of words that have the maximum length
def get_longest_words(string_list):
    max = 0
    answer = []
    for word in string_list:
        if len(word) == max: #don't need to check if reducible, doing that in main()
            answer.append(word)
        if len(word) > max:
            max = len(word)
            answer = []

def main():
    # create an empty word_list
    word_list = []

    # read words from words.txt and append to word_list
    # This is an alternative way to input()
    # since sys.stdin is standard input, and standard input
    # can be treated like a file.
    # Recall that standard input is just your terminal,
    # or whatever file you use input redirection with
    for line in sys.stdin:
        line = line.strip()
        word_list.append(line)

    # find length of word_list
    size = len(word_list)
    # determine prime number N that is greater than twice
    # the length of the word_list
    N = 
    # create an empty hash_list
    hash_table = {}
    # populate the hash_list with N blank strings
    for i in range(len(N)):
        hash_table[i] = ""
    # hash each word in word_list into hash_list
    # for collisions use double hashing 
    for word in word_list:
        insert_word(word, hash_table)
    # create an empty hash_memo of size M
    # we do not know a priori how many words will be reducible
    # let us assume it is 10 percent (fairly safe) of the words
    # then M is a prime number that is slightly greater than 
    # 0.2 * size of word_list
    M = 
    hash_memo = {}
    # populate the hash_memo with M blank strings
    for i in range(len(M)):
        hash_memo[i] = ""
    # create an empty list reducible_words
    reducible_words = []
    # for each word in the word_list recursively determine
    # if it is reducible, if it is, add it to reducible_words
    # as you recursively remove one letter at a time check
    # first if the sub-word exists in the hash_memo. if it does
    # then the word is reducible and you do not have to test
    # any further. add the word to the hash_memo.
    for word in word_list:
        if is_reducible(word):
            reducible_words.append(word)
    # find the largest reducible words in reducible_words
    max = get_longest_words(reducible_words)
    # print the reducible words in alphabetical order
    # one word per line
    for word in max: #not sure if I need to sort to make alphabetical
        print(word)

if __name__ == "__main__":
    main() 