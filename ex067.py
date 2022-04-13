c = 0
while True:
    n = int(input('Digite o valor para calcular a tabuada: '))
    if n < 0:
        print('-'*30)
        print('Fim. Você digitou um número negativo')
        break
    while c < 11:
        tabuada = n * c
        print(f'{n}x{c} = {tabuada}')
        c += 1
    c = 0

'''while True:
    n = int(input('Digite o valor para calcular a tabuada: '))
    if n < 0:
        print('-'*30)
        print('Fim. Você digitou um número negativo')
        break
    for c in range(1, 11):
        tabuada = n * c
        print(f'{n}x{c} = {tabuada}')'''
