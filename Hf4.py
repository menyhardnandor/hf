import random

szam = random.randint(1,5)
szam2 = int(input('Adj meg egy számot: '))

if szam2 == szam:
    print('Egyenlő')
    
if szam2 > szam:
    print('Nagyobb')
    
if szam2 < szam:
    print('Kissebb')