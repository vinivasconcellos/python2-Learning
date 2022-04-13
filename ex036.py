casa = float(input('Valor da casa: R$'))
salario = float(input('Qual o salário: R$'))
anos = int(input('Em quantos anos você quer pagar? '))
parmes = casa/(anos * 12)
if (parmes > (salario * 0.3)):
    print('Para pagar uma casa de R${:.2f} em {} anos\n a prestação será de R${:.2f}.'.format(casa, anos, parmes))
    print('Empréstimo NEGADO!')
else:
    print('Para pagar uma casa de R${:.2f} em {} anos\n a prestação será de R${:.2f}.'.format(casa, anos, parmes))
    print('Empréstimo será CONCEDIDO!')
