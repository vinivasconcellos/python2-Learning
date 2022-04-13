som = 0
cont = 0
for n in range(1, 500):
    if n % 2 != 0 and n % 3 == 0:
        som = som + n
        cont = cont + 1
print('A soma total é {}.'.format(som))
print('Quantidade de número somados é {}'.format(cont))
