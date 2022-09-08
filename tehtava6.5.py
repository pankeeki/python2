import random


def randomLista(lista):
    lista1 = []
    for x in range(lista):
        lista1.append(random.randint(1, 9999))
    return lista1


def parittomatPois(lista):
    parsedList = []
    for x in lista:
        if x % 2 == 0:
            parsedList.append(x)
    return parsedList


def main():
    lista = int(input('Anna listan pituus: '))
    a = randomLista(lista)
    b = parittomatPois(a)
    print(a)
    print(b)


main()
