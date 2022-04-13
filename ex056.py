somaidade=0
contm=0
maiordidadehomem=0
nomevelho=''
for p in range(1, 5):
    print('--- {}ª Pessoa ---'.format(p))
    nome=str(input('NOME: ')).capitalize()
    idade=int(input('IDADE: '))
    sexo=str(input('SEXO (M/F): '))
    somaidade = somaidade + idade
    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        contm = contm + 1
mi=somaidade/4
print('A média de idade do grupo é {} anos'.format(mi))
print('Ao todo, são {} mulheres com menos de 20 anos'.format(contm))
print('O nome do homem mais velho é {}'.format(nomevelho))
print('e sua idade é {} anos'.format(maioridadehomem))
