'''
EX 016 - Faça um programa para uma loja de tintas.
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados
e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas
e o preço total.
'''
metros = float(input('Informe a metragem a ser pintada [M²]: '))
cobertura = metros / 3
latas = cobertura / 18
if latas <= 1:
    latas = 1.0
print(f'Para uma área de {metros} M² será necessário {latas:.0f} latas de 18l,')
print(f'Sairá pelo valor de R$ {latas * 80:.0f}')

