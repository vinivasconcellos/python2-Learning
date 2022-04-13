from random import randint
v = 0
while True:
    jogador = int(input('Digite um valor PAR ou ÍMPAR: '))
    computador = randint (0, 10)
    total = jogador + computador
    tipo = str(input('PAR [P] ou ÍMPAR [I]?')).strip().upper()[0]
#    tipo = ' '
#    while tipo not in 'PpIi':
#        tipo = str(input('PAR ou ÍMPAR?')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador jogou {computador}. Total de {total}')
    if tipo == 'P' and total%2==0:
        print('Você ganhou!')
        v += 1
    elif tipo == 'I' and total % 2 != 0:
        print('Você ganhou!')
        v += 1
    else:
        print('Game Over. O computador ganhou!')
        break
    print('Jogue novamente...')
print(f'Você venceu {v} vezes.')
