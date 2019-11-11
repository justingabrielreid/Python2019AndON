#!/usr/bin/env python3

#Practicing Input and Output
#Author: Justin Reid

firstName = input("Enter your first name: ")
lastName = input("Enter your last name: ")
age = int(input("Enter your age: "))
if firstName == "Justin":
    print("Hello fellow Justin. We have the same name!")
else:
    print("Welcome {}, we are glad to have you here!".format(firstName))
if lastName == "Reid":
    print("Welcome! A fellow Reid I see. Perhaps we are related.")
else: 
    print("Welcome {0}, {1}. Glad to have you here. I hope you enjoy your stay. ".format(firstName,lastName))
