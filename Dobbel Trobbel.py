import random,string

eyes_of_the_devil = [1,2,3,4,5,6]
dicelist = []
strt = 0
print("-----------------------------------------------------------------------")
bruh = input("Type START to begin or QUIT to quit ")
print("")
if bruh.lower() == "start":
    strt = 1

if strt == 1:
    def throw():
        dice1 = random.choice(eyes_of_the_devil)
        dice2 = random.choice(eyes_of_the_devil)
        dice3 = random.choice(eyes_of_the_devil)
        dice4 = random.choice(eyes_of_the_devil)
        dice5 = random.choice(eyes_of_the_devil)

        dicelist.append(dice1)
        dicelist.append(dice2)
        dicelist.append(dice3)
        dicelist.append(dice4)
        dicelist.append(dice5)

throw()
print("Dice 1 = " + str(dicelist[0]))
print("Dice 2 = " + str(dicelist[1]))
print("Dice 3 = " + str(dicelist[2]))
print("Dice 4 = " + str(dicelist[3]))
print("Dice 5 = " + str(dicelist[4]))
