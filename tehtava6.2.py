import random

tavoite = float(input('Mitä maksimilukua tavoitellaan?'))

def noppa():
    return random.randint(1,tavoite)

def main():
    while True:
        heitto = noppa()
        print(f'Heitit numeron {heitto}.')
        if heitto == tavoite:
            print('Voitit pelin.')
            break
main()