resp = 'S'
contidade = conthomens = contmulheres = 0
while resp in 'Ss':
    idade = int(input('Idade: '))
    sexo = str(input('Sexo M/F: ')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str (input('Sexo M/F: ')).strip().upper()[0]
    if idade > 18:
        contidade += 1
    if sexo in 'Mm':
        conthomens += 1
    elif sexo in 'Ff' and idade < 20:
        contmulheres += 1
    resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while resp in 'Nn':
        break
print(f'Tem {contidade} pessoas maiores de 18 anos.')
print(f'Foram cadastrados {conthomens} homens.')
print(f'Tem {contmulheres} mulheres menores de 20 anos')
