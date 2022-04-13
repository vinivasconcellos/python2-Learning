from datetime import date
atual = date.today().year
cont=0
contn=0
for c in range(1, 8):
    nasc = int(input('Ano de nascimento: '))
    if atual - nasc >= 18:
        cont = cont + 1
    else:
        contn = contn + 1
print('{} pessoas atingiram a maioridade'.format(cont))
print('{} pessoas não atingiram a maioridade'.format(contn))
