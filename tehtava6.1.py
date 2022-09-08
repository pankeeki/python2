import random

def noppa():
    return random.randint(1, 6)

def main():
    while True:
        heitto = noppa()
        print(f'Heitit numeron {heitto}.')
        if heitto == 6:
            print('Voitit pelin.')
            break
main()