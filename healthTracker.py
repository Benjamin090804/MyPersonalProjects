# 7/24/21
# HackTable Project: Health Tracker
# Made by Ben Moskalensky
import time

# The opening text, informing the user of what's going on


def intro():
    print("Welcome to the Health Tracker! I'll be your host, you can call me Mr. Aych. Applaud violently when ready!\n")
    # Delays program by 5 seconds for comedic effect
    time.sleep(3)
    print("Well, I was expecting rousing applause but I suppose that'll do too . . .\n")
    time.sleep(1)

# Collecting some data necessary for later calculations


def getBasicUserData():
    name = input("First and foremost, what's your name? ")
    print("Nice to meet you, " + name + "!")
    age = int(input("Now, let's get your age. How old are you? "))
    print()
    while ((age < 3) or (age > 122)):
        print("Nice, but no", age, "year old is taking " +
              "THIS " + "quiz. Input your age again")
        age = int(input())
    print("Thank you. Now, I'm going to get some other measurements. You can be approximate with these. Do you want me to use the imperial or metric system (American or other measurement system?)")
    measurement = input()
    while (len(measurement) < 1):
        measurement = input()
    print()
    # Isolating the first character and making it case independent allows for more user error.
    measurementDeterminer = measurement[0].lower()
    while (not ((measurementDeterminer == "i") or (measurementDeterminer == "m"))):
        print("I don't think that's an option, sorry")
        measurement = input().lower()
        measurementDeterminer = measurement[0]
    units = ["feet", "pounds"]
    if (measurementDeterminer == "m"):
        units = ["meters", "kilograms"]
    height = float(
        input("Excellent, okay. How tall are you, in " + units[0] + "? "))
    if (measurementDeterminer == "i"):
        inches = int(input("and inches? "))
        height = height * 12 + inches
    print("\nYou're doing great so far. Now for a bit more personal a question.")
    weight = float(input("How much do you weigh, in " + units[1] + "? "))
    print("That'll do it for this round of questioning. Thank you for your time.")
    time.sleep(2)
    print("\n")
    retVals = [str(name), str(age), str(height), str(weight), str(units[0])]
    return retVals

# Processes above collected data


def BMIProcessor(userInfo):
    numHeight = float(userInfo[2])
    numWeight = float(userInfo[3])
    if (userInfo[4] == "meters"):
        numHeight *= 39.3701
        numWeight *= 2.20462

    # 3x - 83 and 3x - 242 --> APPROXIMATE formula for healthy BMI: [0, 1]
    # 5x - 152 and 5x - 171 --> APPROXIMATE formula for slightly unhealthy BMI: [2, 3]
    # 6x - 205 and 6x - 162 --> APPROXIMATE formula for unhealthy BMI: [4, 5]
    # 7x - 215 and 7x - 148 --> APPROXIMATE formula for VERY unhealthy BMI: [6, 7]
    distances = [numWeight - (3 * numHeight - 83), numWeight - (3 * numHeight - 242), numWeight - (5 * numHeight - 152), numWeight - (5 * numHeight - 171),
                 numWeight - (6 * numHeight - 205), numWeight - (6 * numHeight - 162), numWeight - (7 * numHeight - 215), numWeight - (7 * numHeight - 148)]
    smallestIndex = 0
    for i in range(0, len(distances)):
        # Find the index with value CLOSEST to 0: Meaning the index returned will be the CLOSEST formula to accurate
        if abs(distances[i]) < abs(distances[smallestIndex]):
            smallestIndex = i

    # Results
    if smallestIndex == 0 or smallestIndex == 1:
        print("You're in great physical health!")
    elif smallestIndex == 2 or smallestIndex == 3:
        print("You're a bit out of shape, but close to where you should be! Try a flexitarian diet! More information here: https://health.usnews.com/best-diet/best-healthy-eating-diets")
    elif smallestIndex == 4 or smallestIndex == 5:
        print("You're marginally overweight. Don't panic though. Reducing sugary and fat-infused foods by just a bit could go a long way, as well as following Mr. Aych's basic workout regiment 3 days/week for 30 minutes per day.")
        time.sleep(3)
        print("10 repetitions per set")
        time.sleep(0.5)
        workouts = ["1. Dumbbell bench press (3 sets)", "2. Dumbbell head lifts (6 sets)", "3. Dumbbell overhead press (3 sets)", "4. Squats (3 sets)",
                    "5. Lying leg curls (3 sets)", "6. Lat Pressdown (6 sets)", "7. Dumbbell Bicep Curls (3 sets)", "8. Standing calf raise (6 sets)", "9. Crunches (5 sets)"]
        for workout in workouts:
            time.sleep(1)
            print(workout)
    else:
        print("Your weight is somewhat unhealthy. Don't be alarmed. You should, however, if you haven't already, consult a doctor on steps to lower your weight.")
    print("\n")

    shouldCont = input(
        "Thank you for participating in the general portion of my Health Tracker. Would you like more specific evaluation or no? ")
    if (shouldCont[0].lower() == "y"):
        return True
    else:
        print("That's all, folks!")
        return False

   # Optional follow-up quiz for specific body health


def physicalHealthEval(name):
    print("Hello, I, Mr. Aych, am back! Happy to see you too, " + name + ".\n")

    # hamstrings
    knowsHamStrings = input(
        "Do you know where your hamstrings are? ")[0].lower()
    if (knowsHamStrings == "n"):
        print("Hamstrings are the muscle groups located around your thighs.\n")
    # if (knowsHamStrings == "y"):
    #     print("Great!\n")
    testHamStrings = input("Do you know how to test if they are strong? ")[
        0].lower()
    print("\n")
    if (testHamStrings == "n"):
        print("Bend over & see if you can touch your fingers and toes.\nThey are strong if you can, and aren't if you can't.\n")
    # if (testHamString == "y"):
    #     print("Great!\n")
    strongHamStrings = input("Are your hamstrings strong? ").lower()[0]
    if (strongHamStrings == "n"):
        print("Try 3 sets, 5 - 15 reps per set (depending on your comfort level) of squats and/or deadlifts, 4 days per week for a month. It shouldn't be too high intensity, but will help strengthen that muscle group.")
    else:
        print("Great!")

    # Conclusion
    print("\nThat brings us to the end of the Health Tracker! Stay healthy and try to have fun doing it!")


def main():
    intro()
    userData = getBasicUserData()
    if (BMIProcessor(userData)):
        physicalHealthEval(userData[0])


if __name__ == "__main__":
    main()
