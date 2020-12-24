import random
name = input("What is your name?: ");      #Get try/except and while loop to ask if users info is correct
response = input('Hello ' + name + ', Would you like to play a number guessing game, or would you like to use \
the maintenance calorie calculator?\nEnter "game" or "calculator to begin: ');
if response == ("game"):
    correctNum = random.randint(0, 20);
    numOfGuess = 0;
    while numOfGuess < 5:
        guess = input("Guess a number from 0 - 20. You have 5 tries: ") #implement how many tries left counter
        numOfGuess += 1;
        if int(guess) < (correctNum):
            print ("To Low, Try a higher number!");
        elif int(guess) > (correctNum):
            print ("To High, Try a lower number!");
        elif int(guess) == (correctNum):
            print ("Great job, you guessed the correct number. ");
            break
    #reponse = ("calculator")
    print ("The number was " + str(correctNum) + ".");
    print ("Thanks for playing!");

else:
    response == ("calculator"); #get upper lower to work with or?
    sedentaryNum = 12.5;
    lightNum     = 14.4;
    moderateNum  = 15.4;
    activeNum    = 16.2;
    extraNum     = 19.9;
    calReq = 0;
    weight = input("What is your weight: ");
    weightInt = (int(weight));
    gender = input('What is your gender? Enter "male" or "female": ');
    if (gender) == ("male"):
        activityLvl = input('What is your activity level?: \
Pick "s","l","m","a",or "e" \nSedentary(0 active days):    Type "s"\nLight(1-3 active days):      Type "l"\nModerate(4-5 active days): \
  Type "m"\nActive(5-6 active days):     Type "a"\nExtraActive(6-7 active days):Type "e"\n');
        if (activityLvl) == ("s"):
            calReq = int(weightInt * sedentaryNum);
            print (name + " You need to eat around " + str(calReq) + " Calories to maintain your current weight."); 
        elif (activityLvl) == ("l"):
            calReq = int(weightInt * lightNum);
            print (name + " You need to eat around " + str(calReq) + " Calories to maintain your current weight.");
        elif (activityLvl) == ("m"):
            calReq = int(weightInt * moderateNum);
            print (name + " you need to eat around " + str(calReq) + " Calories to maintain your current weight.");
        elif (activityLvl) == ("a"):
            calReq = int(weightInt * activeNum);
            print (name + " you need to eat around " + str(calReq) + " Calories to maintain your current weight.");
        elif (activityLvl) == ("e"):
            calReq = int(weightInt * extraNum);
            print (name + " you need to eat around " + str(calReq) + " Calories to maintain your current weight.");
    elif (gender) == ("female"):
        sedentaryNum = 11.4;
        lightNum = 13.1;
        moderateNum = 13.9;
        activeNum = 14.7;
        extraNum = 18.1;
        activityLvl = input('Nice pick ' + name + ', what is your activity level? \
            Pick "s","l","m","a",or "e"or \nSedentary(0 active days):    Type "s"\nLight(1-3 active days):      Type "l"\n\
Moderate(4-5 active days):   Type "m"\nActive(5-6 active days):     Type "a"\nExtraActive(6-7 active days):Type "e"\n');
        if (activityLvl) == ("s"):
            calReq = int(weightInt * sedentaryNum);
            print (name + " You need to eating around " + str(calReq) + " Calories to maintain your current weight."); 
        elif (activityLvl) == ("l"):
            calReq = int(weightInt * lightNum);
            print (name + " You need to eating around " + str(calReq) + " Calories to maintain your current weight.");
        elif (activityLvl) == ("m"):
            calReq = int(weightInt * moderateNum);
            print (name + " you need to eating around " + str(calReq) + " Calories to maintain your current weight.");
        elif (activityLvl) == ("a"):
            calReq = int(weightInt * activeNum);
            print (name + " you need to eating around " + str(calReq) + " Calories to maintain your current weight.");
        elif (activityLvl) == ("e"):
            calReq = int(weightInt * extraNum);
            print (name + " you need to eating around " + str(calReq) + " Calories to maintain your current weight.");
