import random
kleuren = ["ruiten" , "klaveren" , "schoppen" , "ruiten","Joker","Joker"]
cijfers = ["aas","2","3","4","5","6","7","8","9","10","vrouw","boer","koning"]
joebiden=[]
trump=[]
j =0
def aghmmeeetrijkeeren():
    global z
    x = random.choice(kleuren)
    if x != "Joker":
        y = random.choice(cijfers)
    else:
        y = ""
    z = x+" "+y
    return(z,y,x)
while j in range(0,1):
    aghmmeeetrijkeeren()
    if z not in joebiden or trump:
        for t in range (0,7):
            aghmmeeetrijkeeren()
            joebiden.append(z)
            t +=1
        for t in range(8,54):
            aghmmeeetrijkeeren()
            trump.append(z)
            t+=1
        j +=1
print("Gekozen Kaarten " + joebiden)
print("Deck: " + trump)