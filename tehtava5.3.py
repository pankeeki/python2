luku = int(input('Anna luku. '))
alkuluku = True
if luku == 2:
    alkuluku = True
else:
    for x in range(2, luku, 1):
        if luku % x == 0:
            alkuluku = False
            break
if alkuluku == True:
    print('Lukusi on alkuluku.')
else:
    print('Lukusi ei ole alkuluku.')