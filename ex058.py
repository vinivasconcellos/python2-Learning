from random import choice
lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
escolhido = choice(lista)
print('O valor escolhido aleatório foi ...')
conterr = 0
acertou = False
while not acertou:
    n = int(input('Digite um número entre 0 e 10: '))
    conterr += 1
    if n == escolhido:
        acertou = True
    else:
        if n < escolhido:
            print('Mais...')
        else:
            print('Menos...')
print('Parabéns, você acertou. Foram necessárias {} tentativas.'.format(conterr))
