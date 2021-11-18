import random
from random import randrange
kleuren = {"ruiten" , "klaveren" , "schoppen" , "ruiten"}
for i in range(0,10):
    kleuren["ruiten " + str(i)] = None
for i in range(0,10):
    kleuren["klaveren " + str(i)] = None
print(kleuren)
