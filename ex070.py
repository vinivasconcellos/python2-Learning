total = m1000 = menor = cont = 0
barato = ''
while True:
    produto = str(input('Produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    total += preco
    if preco > 1000:
        m1000 += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Você quer continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Total foi de R${total:.2f}')
print(f'{m1000} produtos custam mais de R$1000')
print(f'O produto mais barato é {barato} e custa R${menor}')
