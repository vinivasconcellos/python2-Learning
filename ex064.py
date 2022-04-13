n = 0
soma = 0
cont = 0
while n < 999:
    n=int(input('Digite um número: '))
    if n != 999:
        soma += n
        cont += 1
print('A soma de {} valores foi {}.'.format(cont, soma))
print('FIM')

'''n = soma = cont = 0
n=int(input('Digite um número: '))
while n != 999:
    n=int(input('Digite um número: '))
    soma += n
    cont += 1
print('A soma de {} valores foi {}.'.format(cont, soma))
print('FIM')'''
