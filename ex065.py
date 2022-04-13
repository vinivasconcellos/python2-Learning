resp = 'S'
media = soma = cont = maior = menor = 0
while resp in 'Ss':
    n=int(input('Digite um numero: '))
    resp=str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
media = soma / cont
print('A média entre os {} números digitados é: {}'.format(cont, media))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))
print('Fim')
