import random, string

def w8woordgen(lengte):
    global w8woord, rs
    w8woord = []
    rs = "@#$%&_?"
    upA = random.randrange(2,6)
    numA = random.randrange(4,7)
    lowA = lengte - (upA+numA+3)
    w8woord += (random.choices(string.ascii_uppercase, k = upA))
    w8woord += (random.choices(string.digits, k = numA))
    w8woord += (random.choices(string.ascii_lowercase, k = lowA))
    random.shuffle(w8woord)
    tres()

def tres():
    for character in w8woord[:3]:
        if character.isnumeric():
            w8woordgen(24)
    else:
        Autismico()

def Autismico():
    if w8woord[0] in rs and w8woord[-1] in rs:
        w8woordgen(24)
        

w8woordgen(24)
print(*w8woord, sep = "")