#!/usr/bin/env python3
"""
Author: Justin Reid
Date: Feb 18th 2020

Purpose: Create a simple function that takes a string as an input and returns every even characater as a capital
and every lowercase char as a lowercase. Challenge is to do this without a loop. 

"""
#define the function wordAlt

def wordAlt(word):
    #work with a list of the word
    list_word = list(word)
    list_word[::2] = list(map(str.upper,list_word[::2]))
    list_word[1::2] = list(map(str.lower, list_word[1::2]))
    return ("".join(list_word))


#test cases
userWord = input("Enter a string, only alphabetical characters please: ")
userWord = str(userWord)
print(wordAlt(userWord))




    

