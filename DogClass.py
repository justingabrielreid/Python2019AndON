#!/usr/bin/env python3
#Author: Justin Reid
#Purpose: Practice classes and object oriented programming
def main():
    
    class Dog:
        species = 'mammal'
        #instance attributes
        #these can be different for each instance
        def __init__(self, name, age, gender):
            self.name = name
            self.age = age
            self.gender = gender
        #example of an instance method.
        def description(self):
            return "This dog's name is {}. His/her age is {} years old.".format(self.name, self.age)
        def speak(self, sound):
            print ("{} says {}.".format(self.name, sound))

    maxi = Dog("Max", 3, "Male")
    bigd = Dog("Delilah", 4, "Female")
    roxy = Dog("Roxy", 9, "Female")

    def getOldestDog(*args):
        return max(args)

    print("The oldest dog is {} years old.".format(getOldestDog(maxi.age, bigd.age, roxy.age)))
    print(maxi.description())
    maxi.speak("Hello Mate!")

main()
