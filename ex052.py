n=int(input('Digite um número: '))
cont=0
for c in range(1, n+1):
    if n % c == 0:
        cont=cont + 1
if cont == 2:
    print('O número {} é divisível {} vezes e então:'.format(n, cont))
    print('o número {} é PRIMO'.format(n))
else:
    print('O número {} é divisível {} vezes e então:'.format(n, cont))
    print('o número {} NÃO é PRIMO'.format(n))
