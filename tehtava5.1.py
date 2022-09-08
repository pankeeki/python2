import random
from random import randint
noppamaara = int(input('Montako noppaa? '))
summa = 0
for x in range (0,noppamaara):
    heitto = random.randint(1,6)
    summa = summa + heitto
    print(f'heitetty {heitto}')
print(f'Lopullinen summa on {summa}.')