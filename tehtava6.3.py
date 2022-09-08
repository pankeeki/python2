def funktio():
    gallonat = float(input('Montako gallonaa? '))
    litrat = float(gallonat * 3.78541178)
    return litrat


def main():
    while True:
        litrat = funktio()
        print(f'{litrat} litraa.')
        if litrat < 0:
            break

main()