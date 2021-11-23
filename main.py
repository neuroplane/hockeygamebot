import random
import statistics

redteam = [5, 8, 8]
blueteam = [7, 5, 9]

def roll(case):
    red20 = random.randint(1, 20)
    blue20 = random.randint(1, 20)
    red = statistics.mean(redteam)*red20
    blue = statistics.mean(blueteam)*blue20
    print("RED THROW: " + str(red20) + ", BLUE THROW: " + str(blue20))
    print("RED " + str(round(red, 0)) + " : " + str(round(blue, 0)) + " BLUE")
    if red > blue:
        print("RED WIN A " + case + "!")
    elif blue > red:
        print("BLUE WIN A " + case + "!")
    else:
        print("SUDDEN DEATH!")

def puckdrop():
    print("TIME FOR A PUCKDROP. ROLL A DICE!")
    roll("PUCKDROP")



puckdrop()