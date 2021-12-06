import random
kaarten = ['kaart 1', 'kaart 2', 'kaart 3','kaart 4', 'kaart 5','kaart 6', 'kaart 7']
klaveren=['klaveren koning','klaveren vrouw', 'klaveren boer', 'klaveren 10','klaveren 9','klaveren 8','klaveren 7','klaveren 6','klaveren 5','klaveren 4','klaveren 3','klaveren 2']
harten=['harten koning','harten vrouw','harten boer', 'harten 10','harten 9','harten 8','harten 7','harten 6','harten 5','harten 4','harten 3','harten 2']
ruiten=['ruiten koning', 'ruiten vrouw', 'ruiten boer','ruiten 10','ruiten 9','ruiten 8','ruiten 7','ruiten 6','ruiten 5','ruiten 4','ruiten 3','ruiten 2']
schoppen=['schoppen koning','schoppen vrouw','schoppen boer','schoppen 10','schoppen 9','schoppen 8','schoppen 7','schoppen 6','schoppen 5','schoppen 4', 'schoppen 3', 'schoppen 2']
deck = klaveren + harten + ruiten + schoppen + ['Joker','Joker']
for A, B in zip(kaarten, random.choices(deck, k = 7)):
    print(A+":",B)
    deck.remove(B)
print('Deck[47 Kaarten]: ',deck)