n=int(input('Primeiro termo: '))
r=int(input('Razão: '))
dec=n+((10-1)*r) #o 10 é referente a quantos números eu quero que mostre, que no exercício são 10
for c in range(n, dec+r, r):
    print('{}'.format(c))
