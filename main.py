import random
import statistics

# STRENGTH - AGILITY - ACCURACY - SPEED
teams = ["RED", "BLUE"]
redteam = [4, 8, 8, 4]
blueteam = [7, 5, 9, 3]
stats = ["STRENGTH", "AGILITY", "ACCURACY", "SPEED"]

def chances():
    for t in range(0, len(teams)):
        for s in range(0, len(stats)):
            print(teams[t] + " " + stats[s] + " " + str(redteam[s]))

chances()

def roll(case, redstat, bluestat):
    red20 = random.randint(1, 10)
    blue20 = random.randint(1, 10)
    red = redstat * red20
    blue = bluestat * blue20
    #blue = statistics.mean(blueteam)*blue20
    while red20 == blue20:
        print("REROLL")
        red20 = random.randint(1, 10)
        blue20 = random.randint(1, 10)
        red = redstat * red20
        blue = bluestat * blue20
    print("RED THROW: " + str(red20) + ", BLUE THROW: " + str(blue20))
    print("RED " + str(round(red, 0)) + " : " + str(round(blue, 0)) + " BLUE")
    if red > blue:
        print("RED WIN A " + case + "!")
        attack("RED")
    elif blue > red:
        print("BLUE WIN A " + case + "!")
        attack("BLUE")
    else:
        print("SUDDEN DEATH!")

def puckdrop():
    print("TIME FOR A PUCKDROP!")
    print("RED STRENGTH: " + str(redteam[0]) + ", BLUE STRENGTH: " + str(blueteam[0]))
    roll("PUCKDROP", redteam[0], blueteam[0])

def attack(attacker):
    print("NOW " + attacker + " IS ON THE ATTACK!")

def shooting():
    print("ENCOUNTER")
    # ОБЯЗАТЕЛЬНО СБРОСИТЬ АТАКУ-ЗАЩИТУ ЕСЛИ БЫЛ ЗАБИТ ГОЛ


puckdrop()