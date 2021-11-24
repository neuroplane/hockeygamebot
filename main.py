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
zones = [1, 2, 3]
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
    print(#attacker[0] +
          "Шансы атакующих: " + str(attackerchance))
    return attackerchance


def defencechance(defender):
    defenderchance = diceroll(defender[1])
    print(#defender[0] +
          "Шансы защиты: " + str(defenderchance))
    return defenderchance


def shootingchance(shooter):
    shooterchance = diceroll(statistics.mean([shooter[1], shooter[3]]))
    print(shooter[0] + " SHOT CHANCE: " + str(shooterchance))
    return shooterchance


def savechance(goalie):
    goaliechance = diceroll(statistics.mean([goalie[2], goalie[4]]))
    print(goalie[0] + " SAVE CHANCE: " + str(goaliechance))
    return goaliechance


def puckdrop():
    print("Итак, вбрасывание шайбы!")
    red = diceroll(redteam[1])
    blue = diceroll(blueteam[1])
    while red == blue:
        red = diceroll(redteam[1])
        blue = diceroll(blueteam[1])
    if red > blue:
        puck = "RED"
    else:
        puck = "BLUE"
    print("Шайба у команды " + puck)
    encounter(puck)


def encounter(puck):
    print("Игровой момент!")
    if puck in redteam:
        attacker = redteam
        defender = blueteam
        print("Красные в атаке! Синие защищаются!")
    else:
        attacker = blueteam
        defender = redteam
        print("Синие в атаке! Красные защищаются!")
    attack = attackchance(attacker)
    defence = defencechance(defender)
    while attack == defence:
        attack = attackchance(attacker)
        defence = defencechance(defender)
    if attack > defence:
        puck = attacker[0]
    else:
        puck = defender[0]
    print("Шайба у команды " + puck)
    time.sleep(3)
    shot(puck)


def shot(puck):
    if puck in redteam:
        shooter = redteam
        goalie = blueteam
        print("Красные в атаке! Синие защищаются!")
    else:
        shooter = blueteam
        goalie = redteam
        print("Синие в атаке! Красные защищаются!")
    shooter = shootingchance(shooter)
    defender = savechance(goalie)
    print("Бросок по воротам!")
    if shooter > defender:
        print("ГООООООЛ!")
        time.sleep(3)
        puck = None
        puckdrop()
    else:
        print("Вратарь отражает бросок!")
        puck = goalie[0]
        encounter(puck)


puckdrop()
