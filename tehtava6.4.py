import random


def summa(lista):
    sum = 0
    for x in lista:
        sum = sum + x
    return sum


def main():
    lista = randomLista(10)
    print(summa(lista))


def randomLista(lenOfLista):
    lista = []
    for x in range(lenOfLista):
        lista.append(random.randint(1, 9999))
    return lista

main()
