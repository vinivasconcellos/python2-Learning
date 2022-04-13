n=int(input('Digite um número: '))
fatorial = n
fat = 1
while fatorial > 0:
    print('{}'.format(fatorial), end='')
    print(' x ' if fatorial > 1 else ' = ', end='')
    fat = fat * fatorial
    fatorial = fatorial - 1
print('{}'.format(fat))
