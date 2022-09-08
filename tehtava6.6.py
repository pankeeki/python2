from math import pi

def arvo(e,d):
    return e/(pi * (d/2) ** 2)

def kysely():
    halkaisija = float(input('Anna pizzan halkaisija: '))
    hinta = float(input('Anna pizzan hinta: '))
    return halkaisija, hinta

def main():
    halkaisija1, hinta1 = kysely()
    arvo1 = arvo(halkaisija1, hinta1)

    halkaisija2, hinta2 = kysely()
    arvo2 = arvo(halkaisija2, hinta2)

    if arvo1 > arvo2:
        print('Ensimmäinen pizza on opiskelijabudjetin valinta.')
    elif arvo2 < arvo1:
        print('Toinen pizza on opiskeljabudjetin valinta.')
    else:
        print('Oho, pizzojen hinta-määräsuhde taitaa olla sama.')
main()