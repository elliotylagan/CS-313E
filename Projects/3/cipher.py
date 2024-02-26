# Name 1: Ryan Schlimme
# EID 1: rjs4499

# Name 2: Elliot Ylagan
# EID 2:epy82

'''
This program implements Rail Fence and Vigenere Encode/Decode
'''


def rail_fence_encode(string, key):
    '''
    Input: string is a string of characters and key is a positive
        integer 2 or greater and strictly less than the length of string
    Output: function returns a single string that is encoded with
        rail fence algorithm
    '''
    lst = list(string)
    encoded = []
    for i in range(key):
        encoded.append(lst[:])  # Necessary to change lists independently
    j = set(range(key))
    row = 0
    reverse = False
    for i in range(len(lst)):
        j.remove(row)
        for q in list(j):
            encoded[q][i] = ""
        if reverse is False:
            row += 1
            j = set(range(key))
        if reverse is True:
            row -= 1
            j = set(range(key))
        if row > key - 1:
            row = key - 2
            reverse = True
            j = set(range(key))
        if row < 0:
            row = 1
            reverse = False
            j = set(range(key))
    answer = []
    for z in encoded:
        answer.append("".join(z))
    return "".join(answer)


def rail_fence_decode(string, key):
    '''
    Input: string is a string of characters and key is a positive
        integer 2 or greater and strictly less than the length of 
        string
    Output: function returns a single string that is decoded with
        rail fence algorithm
    '''
    z = len(string)
    lst = []
    for i in range(z):
        lst.append("")
    decoded = []
    for i in range(key):
        decoded.append(lst[:])  # Necessary to change lists independently
    row = 0
    reverse = False
    for i in range(len(lst)):
        decoded[row][i] = "c"
        if reverse is False:
            row += 1
        if reverse is True:
            row -= 1
        if row > key - 1:
            row = key - 2
            reverse = True
        if row < 0:
            row = 1
            reverse = False
    return rail_fence_process(string, decoded, lst, reverse, key)


def rail_fence_process(string, decoded, lst, reverse, key):
    '''
    Intermediary processing for rail fence decoding
    '''
    index = 0
    x = len(decoded)
    y = len(decoded[0])
    for i in range(x):
        for j in range(y):
            if decoded[i][j] == "c":
                decoded[i][j] = string[index]
                index += 1
            if index > len(string)-1:
                index = 0
    row = 0
    reverse = False
    answer = []
    for i in range(len(lst)):
        if decoded[row][i] != "":
            answer.append(decoded[row][i])
        if reverse is False:
            row += 1
        if reverse is True:
            row -= 1
        if row > key - 1:
            row = key - 2
            reverse = True
        if row < 0:
            row = 1
            reverse = False
    return "".join(answer)


def filter_string(string):
    '''
    Input: string is a string of characters
    Output: function converts all characters to lower case and then
        removes all digits, punctuation marks, and spaces. It
        returns a single string with only lower case characters
    '''
    lst = list(string)
    z = len(lst)
    for i in range(z):
        char = lst[i]
        if char.isalpha():
            if not char.islower():
                lst[i] = char.lower()
        else:
            lst[i] = ""
    return "".join(lst)


def encode_character(p, s):
    '''
    Input: p is a character in the pass phrase and s is a character
        in the plain text
    Output: function returns a single character encoded using the
        Vigenere algorithm. You may not use a 2-D list
    '''
    if ord(p) + ord(s) <= ord("a") + ord("z"):
        return chr(ord(p)+ord(s)-ord("a"))
    else:
        return chr(ord(s)+ord(p)-123)


def decode_character(p, s):
    '''
    Input: p is a character in the pass phrase and s is a character
        in the cipher text
    Output: function returns a single character decoded using the
        Vigenere algorithm. You may not use a 2-D list
    '''
    if ord(s)-ord(p) <= 0:
        return (chr(ord(p)-ord(s)+ord("a")))
    else:
        return chr*(ord(p)-ord(s)+ord("z")+1)


def vigenere_encode(string, phrase):
    '''
    Input: string is a string of characters and phrase is a pass phrase
    Output: function returns a single string that is encoded with
        Vigenere algorithm
    '''
    string = filter_string(string)
    phrase = filter_string(phrase)
    string_list = list(string)
    phrase_list = []
    i = 0
    while len(string_list) != len(phrase_list):
        try:
            phrase_list.append(phrase[i])
        except IndexError:
            i = -1
        i += 1
    answer = []
    for s, p in zip(string_list, phrase_list):
        answer.append(encode_character(p, s))
    return "".join(answer)  # placeholder for the actual return statement


def vigenere_decode(string, phrase):
    '''
    Input: string is a string of characters and phrase is a pass phrase
    Output: function returns a single string that is decoded with
        Vigenere algorithm
    '''
    string = filter_string(string)
    phrase = filter_string(phrase)
    string_list = list(string)
    phrase_list = []
    i = 0
    while len(string_list) != len(phrase_list):
        try:
            phrase_list.append(phrase[i])
        except IndexError:
            i = -1
        i += 1
    answer = []
    for s, p in zip(string_list, phrase_list):
        answer.append(decode_character(p, s))
    return ""  # placeholder for the actual return statement


def main():
    '''
    Executes the body of the program. Encodes and decodes text as specified
    by instructions. Reads plain text from standard input.
    '''
    print()
    print("Rail Fence Cipher")
    print()

    text = input("Plain Text: ")
    key = input("Key: ")
    rail_encode = rail_fence_encode(text, key)

    print("Encoded Text:", rail_encode)
    print()

    encode = input("Encoded Text: ")
    key = input("Key: ")
    rail_decode = rail_fence_decode(encode, key)

    print("Decoded Text:", rail_decode)
    print()

    print("Vigenere Cipher")
    print()

    text = input("Plain Text: ")
    phrase = input("Pass Phrase: ")
    vigenere_scramble = vigenere_encode(text, phrase)

    print("Encoded Text:", vigenere_scramble)
    print()

    encode = input("Encoded Text: ")
    phrase = input("Pass Phrase: ")
    vigenere_normal = vigenere_decode(encode, phrase)

    print("Decoded Text:", vigenere_normal)


# The line above main is for grading purposes only.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()
