def calculateBMR(age, height, weight, gender):
    if(gender == "male"):
        bmr = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
    elif(gender == "female"):
        bmr = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)

    return bmr

def calculateBMI(height, weight):
    bmi = weight / (height * height)

    if(bmi <= 18.5):
        result = "Under Weight"
    elif(bmi > 18.5 and bmi < 24.9):
        result = "Normal Weight"
    elif(bmi > 25 and bmi < 29.9):
        result = "Overweight"
    elif(bmi > 30):
        result = "Obesity"
    
    return result

def activityFactor(activity,bmr):
    if(activity == "sedentary"):
        activityresult = bmr * 1.2
    elif(activity == "lightly active"):
        activityresult = bmr * 1.375
    elif(activity == "moderately active"):
        activityresult = bmr * 1.55
    elif(activity == "very active"):
        activityresult = bmr * 1.725
    elif(activity == "extra active"):
        activityresult = bmr * 1.9

    return activityresult

def TDEE(BMR, ActivityFactor):
    # To find out user maintenance calories (Total Daily Energy Expenditure)
    tdee = BMR + ActivityFactor
    return tdee

def goal(Tdee, goalChoice):
    if(goalChoice == "muscle building" or goalChoice == "weight gain"):
        goalresult = Tdee + (Tdee/100 * 10)
    elif(goalChoice == "weight loss"):
        goalresult = Tdee - (Tdee/100 * 20)
    
    return goalresult

def exercise(goalChoice):
    muscleBuildingExercises = ["Deadlifts", "Bench Press", "Barbell Curl", "Squats", "Push Ups", "Pull Ups"]
    weightLossExercises = ["Running", "Cycling", "Swimming", "Jump Rope", "HIIT Workouts"]
    weightGainExercises = ["Powerlifting", "Bodybuilding", "Resistance Training", "High-Intensity Interval Training"]

    if (goalChoice == "muscle building"):
        return muscleBuildingExercises
    if (goalChoice == "weight loss"):
        return weightLossExercises
    if (goalChoice == "weight gain"):
        return weightGainExercises

def display(name, Tdee, BMI, Goal, goalChoice, exerciseRecommendation):
    print(f"\n{name}, according to your given information currently you are {BMI}.")
    print(f"\n Your Total Daily Energy Expenditure is {Tdee:.2f} cal")
    print(f"\n To achieve your goal: {goalChoice}, you need to consume {Goal:.2f} cal per day.")
    print(f"\n Recommended Exercises for {name}:")
    for exercise in exerciseRecommendation:
        print(f"- {exercise}")

def main():
    name = input("Enter your name: ")
    age = int(input("\nEnter your age: "))
    height = float(input("\nEnter your height in cm: "))
    weight = float(input("\nEnter you weight: "))
    gender = input("\nEnter your Gender: ").lower()

    print("\nHow often do you exercise?\n")
    print("Sedentary: minimal or no exercise\n")
    print("Lightly active: lightly one to three days a week\n")
    print("Moderately active: moderately three to five days a week\n")
    print("Very active: Six to seven days a week\n")
    print("Extra active: Very hard exercise six to seven days a week or have a physical job\n")
    activity = input(">").lower()

    BMR = calculateBMR(age, height, weight, gender)
    BMI = calculateBMI(height, weight)
    ActivityFactor = activityFactor(activity, BMR)
    Tdee = TDEE(BMR, ActivityFactor)

    print("\nWhat's your goal?")
    print("\nMuscle Building")
    print("\nWeight Loss")
    print("\nWeight Gain")
    goalChoice = input(">").lower()

    Goal = goal(Tdee, goalChoice)
    exerciseRecommendation = exercise(goalChoice)

    display(name, Tdee, BMI, Goal, goalChoice, exerciseRecommendation)

main()