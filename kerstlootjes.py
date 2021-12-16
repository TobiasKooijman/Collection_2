import random, time
## PRINT INTRO ##
print("_____________________________________________________________________________________________________________")
print("")
print("KERSTLOOTJES")
print("VOER JE NAAM IN EN DOE MEE!!")
print("STIK!  (Type QUIT to quit.)")
print("")

## Variables ##
Names = []

## Functions ##
def Questions():
    naam = input('Naam: ')
    Names.append(naam)
    while naam.lower() != "quit":
        naam = input('Naam: ')
        Names.append(naam)
Questions()
del Names[-1]
if len(Names) < 2:
    print("Je hebt te minste 2 namen nodig")
    Questions()
    del Names[-1]
time.sleep(0.3)
## Print Interval ##
print("")
print("Current names: ")
print(', '.join(Names))
print("--------------------------------------")
time.sleep(0.2)
print("Shuffeling...")
time.sleep(2)
print("Lijst:")
print("-----------------------------------")
gedaan = []
for n in Names:
    mogelijk = []
    mogelijk = list(set(Names) - set(gedaan))
    try:
        mogelijk.remove(n)
    except:
        pass
    rand = random.randint(0, (len(mogelijk))-1)
    randomMog = mogelijk[rand]
    gedaan.append(randomMog)
    print("%s heeft %s" % (n, randomMog))