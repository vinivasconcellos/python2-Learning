n = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termo = n
cont = 1
while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo = termo + r
    cont += 1
print('FIM')
