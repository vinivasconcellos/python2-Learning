n = int(input('Digite um número entre 1 e 10: '))
for c in range(0, 11):
    tabuada=c*n
    print('{}x{} = {}'.format(n, c, tabuada))
