""" An interactive dictionary made by using Python   """

import json
import difflib
from difflib import get_close_matches  ## Importing the close match algorithm

data = json.load(open("data.json")) ## Loading the json dataset in the app. Dataset is in form of dictionary.

print ("An interactive dictionary made by using Python")

    ## Function which finds the word within the dataset
def find_word(word):
    if word in data:
        return (data[word])
    elif len(get_close_matches(word, data.keys())) :  ## using the function for keys in dictionary
        yn = input("Did you mean "+ get_close_matches(word, data.keys(), cutoff= 0.8)[0]+ " instead? Enter Y if yes and N if no. ")
        if yn == "Y" or yn == "y":
            return data[get_close_matches(word, data.keys(), cutoff= 0.8)[0]]
        elif yn == "N" or yn == "n":
            return "The word dosen't exists. Please double check it."
        else:
            return "We didn't understand your query"
    else:  ## If input is some random word, then promt the user
        return "The word dosen't exists or is not valid. Please double check it."


word = (input("Enter word: ")).lower() ## Asking input from user and converting into lowercase
output = (find_word(word))
if type(output) == list:    ## to give each word definition in a new line if output is list
    for index, value in enumerate(output, 1): ## numbering bullets starting from 1 (enumerate function to start indexing from 1)
        print("{}. {}".format(index, value))
else:
    print(output)
