def twoWords(length, firstLetter):
    firstWord = ""
    secondWord = ""

    while True:
        firstWord = input("a " + str(length) + " letter word please: ")
        if length == len(firstWord):
            break
    while True:
        secondWord = input("a word begining with " + firstLetter + " please: ")
        if secondWord[0] == firstLetter.upper() or secondWord[0] == firstLetter.lower():
            break

    return [firstWord, secondWord]
print(twoWords(4,"b"))


def twoWordsV2(length, firstLetter):
    
    wordList = []
    t = True
    while t: 
        t1 = input('Enter a ' + str(length) + '-letter word please: ')
        if length == len(t1):
            wordList.append(t1)
            t = False
        else:
            continue
    t = True
    while t:
        t2 = input('Enter a word beginning with ' + str(firstLetter) + ' please: ')
        if t2[0] == firstLetter:
            wordList.append(t2)
            t = False
        else:
            continue
    return wordList
print(twoWordsV2(4,'b'))

def enterNewPassword():
    
    while True:
        password = input("Enter a password: ")
        if len(password) >= 8 and len(password) <=15 and any(char.isdigit() for char in password):
            print ("Accepted")
            break 
        else:
            print("Password is not between 8 and 15 characters and/or one digit")
enterNewPassword()

import random
num = random.randint(0,50)
while True:
    for i in range(5):
        attempt = int(input("Guess a number in the range of 0-50!: "))
        if attempt == num:
            print("Nice Job, you got it!")
        else:
            if attempt > num:
                print("your guess is too high.")
            else:
                print("your guess is too low.")
    print("The number was: " + str(num))
                    
