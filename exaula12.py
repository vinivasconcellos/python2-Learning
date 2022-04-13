nome = str(input('Qual é seu nome? '))
if nome == 'Vinícius':
    print('Que nome bonito!')
elif nome == 'Lena' or nome == 'Gustavo' or nome == 'Simone':
    print('Seu nome é bem popular.')
elif nome in 'Maria Ana Cláudia Augusto':
    print('Belo nome.')
#else:
    #print('Seu nome é normal.')
print('Tenha um bom dia {}!'.format(nome))
