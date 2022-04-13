n = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
termo = n
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo = termo + r
        cont += 1
    print('PAUSA')
    mais=int(input('Quantos termos a mais você quer? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))
print('FIM')
#if mais != 0:
    #termo = termo + r
    #   con = 1
    #while con <= mais:
    #   print('{} -> '.format(termo), end='')
    #    termo += r
#    con += 1
