cont = soma = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'A soma de {cont} números digitados é {soma}.')
