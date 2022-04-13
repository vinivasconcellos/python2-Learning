soma=0
cont=0
for c in range(1, 7):
    n = int(input('N: '))
    if n%2==0:
        soma=soma+n
        cont=cont+1
print('Você informou {} números PARES e a soma total é: {}'.format(cont, soma))
