#!/usr/bin/env python3
#Basic class example problem
#Author: Justin Reid 
#Date Sat Nov 2nd 2019 

class Dog:
    #initiate the class
    def __init__(self,name,age):
        self.name = name
        self.age = age
    #initiate method    
    def agein2year(self):
        return self.age + 2

roxy = Dog("Roxy", 8)

print("{}'s age in two years will be {} years old.".format(roxy.name, roxy.agein2year()))

