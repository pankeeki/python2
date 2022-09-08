lista = []
syote = None
while True:
    syote = input('Anna luku. Tyhjä syöte opettaa ohjelman. ')
    if (syote == ''):
        break
    else:
        lista.append(int(syote))
lista.sort(reverse=True)
print(lista[0:5])