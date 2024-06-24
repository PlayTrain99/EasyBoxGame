import random
from enum import Enum

def findApproximateValue(value, percentRange):
    lowestValue =  value - (percentRange/100) * value
    maxValue =  value + (percentRange/100)* value
    return random.randint(int(lowestValue), int(maxValue))


Event = Enum('Event', ['Chest', 'Empty'])

evnetDictionart = {
    Event.Chest: 0.6,
    Event.Empty: 0.4
}

eventList = tuple(evnetDictionart.keys())
eventProbablity = tuple(evnetDictionart.values())

Colors = Enum("Colors", {'Green':'zielony', "Orange":"pomarńczowy", "Red":"czerwony"})

chestColorsDictionart = {
    Colors.Green: 0.75,
    Colors.Orange: 0.2,
    Colors.Red: 0.05
}

ColorsList = tuple(chestColorsDictionart.keys())
ColorsProbablity = tuple(chestColorsDictionart.values())

rewordsForChests = {
    ColorsList[reward]: (reward + 1) * (reward + 1) * 1000
    for reward in range(len(ColorsList))
}

gameLenght = 5 
goldAcquired = 0

print("Komnata Game!!!")
print("You have only 5 step, to find gold.")

while gameLenght > 0:
    gamerAnser = input("Do you want to move forward: ")
    if (gamerAnser == "yes"):
        print("Great, let's see waht you got ...")
        drawnEvent = random.choices(eventList, eventProbablity)[0]
        if (drawnEvent == Event.Chest):
            print("You have Chest!")
            drownColors = random.choices(ColorsList, ColorsProbablity)[0]
            print(f"The ches colors is {drownColors.value}.")
            gameReward = findApproximateValue(rewordsForChests[drownColors], 10)
            goldAcquired = goldAcquired + gameReward
        elif(drawnEvent == Event.Empty):
            print("You have nothing. Sorry!")
    else:
        print("You can go just stright!!!")
        continue

    gameLenght = gameLenght - 1

print(f"FYeahh, you end thje Game. You'er gold {goldAcquired}.")