from time import sleep
n1=int(input('N1: '))
n2=int(input('N2: '))
maior = 0
selecao = 0
while selecao != 5:
    print('[1] para somar')
    print('[2] para multiplicar')
    print('[3] o maior')
    print('[4] informar novos números')
    print('[5] sair do programa')
    selecao=int(input('Item: '))
    if selecao == 1:
        soma = n1 + n2
        print('Soma = {}'.format(soma))
    else:
        if selecao == 2:
            mult = n1 * n2
            print('Multiplicação = {}'.format(mult))
        else:
            if selecao == 3:
                if n1 > n2:
                    maior = n1
                    print('O maior é {}'.format(maior))
                else:
                    maior = n2
                    print('O maior é {}'.format(maior))
            else:
                if selecao == 4:
                    n1 = int(input('Informe novo N1: '))
                    n2 = int(input('Informe novo N2: '))
                else:
                    if selecao == 5:
                        print('Finalizando...')
                        sleep(2)
                    else:
                        print('Opção inválida. Tente novamente')
                    sleep(1)
print('Fim do programa!')
