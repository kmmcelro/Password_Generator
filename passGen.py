# Author: Kaitlin McElroy
# Purpose: To generate a random password with a variety of characteristics using the command line
# Date: November 22, 2023
import random
import string
        
# Random letter selection, accounts for uppercase and lowercase letters
def randLetters(num, upperFlag):
    letters = string.ascii_lowercase   
    if upperFlag:
        upperLet = string.ascii_uppercase
        upperNum = random.randint(1,num-2)
        lowerNum = num - upperNum
        rand_letters = random.choices(letters,k=lowerNum) + random.choices(upperLet,k=upperNum)
    else:
        rand_letters = random.choices(letters,k=num) 
    return rand_letters

# Makes the password accounting for the different settings
def makePassword(passwordSz, upperFlag, numFlag, symFlag):
    if symFlag and numFlag:
        numLets = random.randint(3,passwordSz-2)
        numNums = random.randint(1,passwordSz-numLets-1)
        numSyms = passwordSz - numLets - numNums
    elif symFlag:
        numLets = random.randint(3,passwordSz-1)
        numNums = 0
        numSyms = passwordSz - numLets 
    elif numFlag:
        numLets = random.randint(3,passwordSz-1)
        numNums = passwordSz - numLets
        numSyms = 0
    else:
        numLets = passwordSz
        numNums = 0
        numSyms = 0
    passList = randLetters(numLets, upperFlag)  + random.choices(string.digits,k=numNums) + random.choices(string.punctuation,k=numSyms)
    random.shuffle(passList)
    password = "".join(passList)
    return password

# Inputting the password size 
while True:
    try:
        passwordSz = int(input("How long does your password need to be?\n"))
        break
    except ValueError:
        print("Please input a number.\n")

# Inputting whether or not there should be uppercase letters
while True:
    upperInput = input("Do you need uppercase letters?\n")
    if upperInput == "y" or upperInput == "yes":
        upperFlag = True
        break
    elif upperInput == "n" or upperInput == "no":
        upperFlag = False
        break

# Inputting whether or not there should be numbers
while True:
    numInput = input("Do you need numbers?\n")
    if numInput == "y" or numInput == "yes":
        numFlag = True
        break
    elif numInput == "n" or numInput == "no":
        numFlag = False
        break
    
# Inputting whether or not there should be symbols
while True:
    symInput = input("Do you need symbols?\n")
    if symInput == "y" or symInput == "yes":
        symFlag = True
        break
    elif symInput == "n" or symInput == "no":
        symFlag = False
        break

# Makes the user update the password length if it's too short otherwise it makes the password
while True:
    try: 
        password = makePassword(passwordSz, upperFlag, numFlag, symFlag)
        break
    except:
        if upperFlag and numFlag and symFlag:
            passwordSz = int(input("You need a longer password. Please input a bigger number. Mininum is 5.\n"))
        elif upperFlag and (numFlag or symFlag):
            passwordSz = int(input("You need a longer password. Please input a bigger number. Mininum is 4.\n"))
        elif upperFlag or numFlag or symFlag:
            passwordSz = int(input("You need a longer password. Please input a bigger number. Mininum is 3.\n"))
print(password)
