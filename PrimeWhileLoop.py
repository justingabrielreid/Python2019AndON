#!/usr/bin/env python3

def main(): 
    num = int(input("Enter a number to test if it is prime: "))
    test = 2

    while test < num:
        if num % test == 0 and num != test:
            print("{} is not a prime number!".format(num))
            break
        test += 1
    else:
        print("{} is a prime number!".format(num))

main()

