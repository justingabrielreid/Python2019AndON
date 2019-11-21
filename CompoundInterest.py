#!/usr/bin/env python3
#Author Justin Reid
#Purpose. Practice and a simple program that will make predictions on how much you need to save to retire 
#with five million. 
#Will gradually update to practice my programming skills. 

#note: This is a perfect little project that can be used to improve my programming skills. 
#immediate improvements that could be made: 
"""
1. delay the print statements by a few seconds. 
2. prettier text for the print statements. 
3. print the savings needed result better. 
"""
def main():
    #importing a few libraries to delay the print statements. 
    
    #Introductory Statements to the User. 
    
    print("Hello.")
    #these need work. Not delaying enough
    print("Welcome to the compound interest tracker.")
    print()
    print("This program will allow you to make predictions on how much is needed to be saved each month.")
    print()
    userName = input("Can I have your name? ")
    #Error check to ensure the input is valid. A string. 
    print(" ")
    #validating input for the age
    def ageChecker(name):
        import sys
        while True:
            try:
                ageUser = int(input("Hello {}, can I have your age? ".format(name)))
            except ValueError:
                print("I need a whole number for the calculation!")
                continue
            else:
                if ageUser <= 0:
                    print("Thank you {} but that is not a valid age.".format(userName))
                    continue
                elif ageUser >= 67:
                    print("Thank you for using the program but you are older than 67!")
                    sys.exit()
                elif ageUser < 18:
                    print("Thank you but you are a bit too young. Come back when 18 or older!")
                    sys.exit()  
                else:
                    return ageUser
                    break
    def principalChecker():
        import sys
        while True:
            try: 
                principal = float(input("What is your starting investment? "))
            except ValueError:
                print("I need an actual number to perform the calculation! ")
                continue
            else:
                if principal <= 0:
                    print("I need a positive number!")
                    continue
                elif principal >= 5000000.0:
                    print("You are already set! Rich ass nigga!")
                    sys.exit()
                else:
                    return principal
                    break
    def savingsCalculator(currentAge, startingInvestment):
        moneyTarget = 5000000.0
        targetAge = int(67)
        interestRate = 0.098
        yearsLeft = targetAge - currentAge
        savePerYear = (moneyTarget - startingInvestment*(1+interestRate)**yearsLeft) / (yearsLeft*(1+interestRate)**yearsLeft)
        return round(savePerYear,2)
    age = ageChecker(userName)
    initialInvest = principalChecker()
    savings = savingsCalculator(age, initialInvest)
    print(savings)
   #print("This is what you will need to save per year: ".format(savings)) 
main()

#
#
#
#
#
