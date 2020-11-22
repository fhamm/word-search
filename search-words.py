import sys

query = sys.argv[1]
#dictionary_name = sys.argv[2]
dictionary_name = './dictionaries/pt-br-ascii.txt'

# --- #

consonant_list = ['B', 'C', 'D', 'F', 'G', 'H', 
        'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 
        'T', 'V', 'W', 'X', 'Y', 'Z']

vowel_list = ['A', 'E', 'I', 'O', 'U']

consonant_marker = '_'
vowel_marker = '@' 

# --- #

def rectify(string):
    string = string.upper()
    string = string.rstrip()
    return string

def findWords(query, dictionary_name):
    dictionary = open(dictionary_name, 'r')
    query = rectify(query)
    for word in dictionary.readlines():
        word = rectify(word)
        match = True
        for index, letter in enumerate(word):
            if len(query) != len(word):
                match = False
                break
            elif query[index] == consonant_marker and word[index] in vowel_list:
                match = False
                break
            elif query[index] == vowel_marker and word[index] in consonant_list:
                match = False
                break
            elif query[index] != consonant_marker and query[index] != vowel_marker and query[index] != word[index]:
                match = False
                break
        if match:
            print(word)

findWords(query, dictionary_name)
