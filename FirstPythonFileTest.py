import random
name = input("What is your name?: ");
age = input ("What is your age?: ");
dateOfBirth = input("What is your DOB?: ");
print ("Your information is as stated below: \n"
       + "Name: " + name + "\nAge: " + age + "\nDate Of Birth: " + dateOfBirth);
print ("Awesome " + name + "! " + "Now lets get started! ");
response = input('Would you like to play a number guessing game? Or do you need a diet macro Calculator? Enter "game" or "calculator": ');
if response == ("game"):
    correctNum = random.randint(0, 20);
    numOfGuess = 0;
    while numOfGuess < 3:
        guess = input("Nice pick " + name + ", now guess a number from 0 - 20: ")
        numOfGuess += 1;
        if int(guess) < (correctNum):
            print ("To Low, Try a higher number!");
        elif int(guess) > (correctNum):
            print ("To High, Try a lower number!");
        else:
            int(guess) == (correctNum);
            print ("nice!");
            break
print ("The number was " + str(correctNum) + "!");
