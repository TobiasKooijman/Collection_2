vraag = "bruh"
vraag2 = "joe Biden"
lijst = {}
print("--------------------------")
print("type (klaar) als je klaar bent!")
print("")
vraag = str(input('Wat wil je bestellen? '))
vraag2 = int(input('Hoeveel wil je daarvan bestellen? '))

if vraag != "klaar":
        lijst[vraag] = vraag2
while vraag != "klaar":
    vraag = str(input('Wat wil je nog meer bestellen? '))
    if vraag == "klaar":
        break
    vraag2 = int(input('Hoeveel wil je daarvan bestellen? '))
    if vraag2 == "klaar":
        break
    if vraag in lijst.keys():
        lijst[vraag] = lijst[vraag] + vraag2
    if vraag not in lijst.keys():
        lijst[vraag] = vraag2
print("")
print("Boodschappenlijstje: ")
print(lijst)
