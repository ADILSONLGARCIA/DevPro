# 011. Faça um Programa que peça 2 números inteiros e um número real.
# Calcule e mostre:
# o produto do dobro do primeiro com metade do segundo .
# a soma do triplo do primeiro com o terceiro.
# o terceiro elevado ao cubo.
n1 = int(input('Informe um número inteiro:'))
n2 = int(input('Informe outro número inteiro:'))
r1 = float(input('Informe um número Real:'))
calc_1 = (n1 * 2) + (n2 / 2)
calc_2 = (n1 * 3) + r1
calc_3 = r1 ** 2
print(f'O dobro do primeiro valor {n1} com metade do segundo valor {n2}, resulta no produto {calc_1}')
print(f'A soma do triplo do primeiro valor {n1} com o valor do terceiro {r1} resulta no produto {calc_2}.')
print(f'O terceiro valor {r1} elevado ao cubo é {calc_3:.2f}.')
