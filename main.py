import random
import statistics
import time

# STRENGTH - AGILITY - ACCURACY - SPEED
puck = None
teams = [{"RED": {"strength": 4, "agility": 8, "accuracy": 8, "speed": 4}},
         {"BLUE": {"strength": 7, "agility": 5, "accuracy": 9, "speed": 3}}]
redteam = ["RED", 5, 7, 7, 4]
blueteam = ["BLUE", 7, 5, 8, 3]
stats = ["TEAM", "STRENGTH", "AGILITY", "ACCURACY", "SPEED"]
puck = None

print("TEAM: " + str(redteam[0]) + ", STRENGTH: " + str(redteam[1]) + ", AGILITY: " + str(
    redteam[2]) + ", ACCURACY: " + str(redteam[3]) + ", SPEED: " + str(redteam[4]))
print("TEAM: " + str(blueteam[0]) + ", STRENGTH: " + str(blueteam[1]) + ", AGILITY: " + str(
    blueteam[2]) + ", ACCURACY: " + str(blueteam[3]) + ", SPEED: " + str(blueteam[4]))


def diceroll(stat):
    chance = stat * random.randint(1, 6)
    return chance


# NAME - STRENGTH - AGILITY - ACCURACY - SPEED
def attackchance(attacker):
    attackerchance = diceroll(statistics.mean([attacker[2], attacker[4]]))
    print(attacker[0] + "ATTACK CHANCE: " + str(attackerchance))


def defencechance(defender):
    defenderchance = diceroll(defender[1])
    print(defender[0] + " DEFENCE CHANCE: " + str(defenderchance))


def shootingchance(shooter):
    shooterchance = diceroll(statistics.mean([shooter[1], shooter[3]]))
    print(shooter[0] + " SHOT CHANCE: " + str(shooterchance))


def savechance(goalie):
    goaliechance = diceroll(statistics.mean([goalie[2], goalie[4]]))
    print(goalie[0] + " SAVE CHANCE: " + str(goaliechance))


def puckdrop():
    print("PUCK DROP")


def encounter():
    print("encounter")


def shot():
    print("SHOT")


print("ENCOUNTER")
attackchance(blueteam)
defencechance(redteam)
print("==========\nSHOOTING")
shootingchance(blueteam)
savechance(redteam)
