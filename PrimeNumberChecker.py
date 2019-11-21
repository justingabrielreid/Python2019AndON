#!/usr/bin/env python3

def main():
    num = int(input("Enter a number: "))
    prime = True 

    for test in range(2,num):
        if num % test == 0 and num != test:
            print(num," equals",test, "*", int(num/test))
            prime = False
    if prime:
            print(num, " is a prime number!")
    else: 
        print("This is not a prime number!")
main()


