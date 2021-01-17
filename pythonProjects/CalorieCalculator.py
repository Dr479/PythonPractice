def userInfo():
    #name = input("What is your name?: ");
    age = int(input("What is your age?: "));
    height = int(input ("What is your height in inches?: "));
    weight = int(input ("What is your weight in pounds?: "));
    gender = input ("What is your gender?: ");

    if  gender == ("female"):
            userG1 = 745
            userHeightM = 4.35 * height;
            userWeightM = 4.7 * weight;
            userAgeM = 4.7 * age;
    elif gender == ("male"):
            userG1 = 430
            userHeightM = 6.2 * height;
            userWeightM = 6.2 * weight;
            userAgeM = 6.75 * age;

    
     #https://en.wikipedia.org/wiki/Harris%E2%80%93Benedict_equation
    bmr = userG1 + userHeightM + userWeightM - userAgeM
    return(int(bmr))

def calculateActivity(bmr): 
    activityLevel = input('Is your activity level "sedentary", "light", "moderate", \
"heavy", "extreme":')

    if activityLevel == ("sedentary"):
        activityLevel = 1.2 * bmr
    elif activityLevel == ("light"):
        activityLevel = 1.375 * bmr
    elif activityLevel == ("moderate"):
        activityLevel = 1.5 * bmr
    elif activityLevel == ("heavy"):
        activityLevel = 1.7 * bmr
    elif activityLevel == ("extreme"):
        activityLevel = 1.82 * bmr

    return(int(activityLevel))

def calOutput(activityLevel):
    goals = input('Do you want to "lose","gain", or "maintain" your weight: ');
    
    if goals == ("lose"):
        lose = input("Do you want to lose 1 or 1.5 pounds a week?: ");
        if lose == "1":
            newCal = activityLevel - 500;
        elif lose == "1.5":
            newCal = activityLevel - 750;   
    elif goals == ("gain"):
        gain = input("Do you want to gain 1 1.5 or 2 pounds a week?: ");
        if gain == "1":
            newCal = activityLevel + 500;
        elif gain == "1.5":
            newCal = acitivtyLevel + 750;
        elif gain == "2":
            newCal = activityLevel + 1000;
    elif goals == ("maintain"):
        newCal = activityLevel;

    print (" In order to " + goals +" weight, you need to eat about ",  (newCal),  " calories");


calOutput(calculateActivity(userInfo()))

