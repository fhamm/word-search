import os
import sys
import unicodedata

input_file_name = sys.argv[1]

def rectify(word):
    # Remove non-ASCII characters
    rectified_word = unicodedata.normalize("NFD", word)
    rectified_word = rectified_word.encode("ascii", "ignore")
    rectified_word = rectified_word.decode("utf-8")
    
    return rectified_word

def isStringNotBlank(string):
    return bool(string.strip())

def generateWordList(input_file_name):
    input_file = open(input_file_name, 'r')
    word_list = []

    # Read file word-by-word
    for word in input_file.readlines():
        rectified_word = rectify(word)
        rectified_word = rectified_word.upper()
    
        # Check if rectified word is blank or already has been added
        if isStringNotBlank(rectified_word):
            if not word_list or rectified_word != word_list[-1]:
                word_list.append(rectified_word)
    
    input_file.close()
    return word_list 

def exportWordList(word_list, output_file_name):
    output_file = open(output_file_name, 'a')
    
    # Append words to file
    for word in word_list:
        output_file.write(word)
    
    output_file.close()

# --- #

word_list = generateWordList(input_file_name)

output_file_name = os.path.splitext(input_file_name)[0] + '-ascii.txt' 
exportWordList(word_list, output_file_name)
