# EXERCÍCIO 017 - Faça um Programa para uma loja de tintas:

# O programa deverá pedir:
# área a ser pintada em M²
# cobertura de 1 litro para 6 M²

# vendida em:
# latas de 18 litros a R$ 80,00
# galões de 3,6 litros a R$ 25,00

# Informe ao usuário:
# as quantidades de tinta a serem compradas e os respectivos preços#

# Nota:
# comprar apenas latas de 18 litros; # comprar apenas galões de 3,6 litros;
# misturar latas e galões, de forma que o desperdício de tinta seja menor.
# Acrescente 10% de folga e sempre arredonde os valores para cima, considere latas cheias.

import math

# solicitandp a área que será pintada
area = int(input('Informe a área a ser pintada (M²): '))

# area com folgas de 10%
folga = area * 1.1

# A tinta rende 6 m² com uma demão de tinta
litros_metro = 6

# Calculo comprando somente latas de 18 litros de tinta
usar_litros = folga / litros_metro
lata18 = 18
n_latas18 = math.ceil( usar_litros / lata18 )
val_lat18 = 80 * n_latas18
print(f'Se você só usar latas de 18 litros terá que compar {n_latas18} latas com um custo de R${val_lat18} ' )

# Calculo usando somente galões de 3.6 litros
galao = 3.6
num_galao = math.ceil(usar_litros / galao)
tot_galao = num_galao * 25
print(f'Usando galões teria que comprar {num_galao} latas com o custo de R$ {tot_galao}')

# Calculo orientado pelo valor
n_latas18 = math.floor(usar_litros/lata18)
val_lat18 = n_latas18 * 80
litros_falta = usar_litros % lata18
num_galao = math.ceil(litros_falta / galao )
val_galao = num_galao * 25
val_total = val_lat18 + val_galao
print(f'Voce deverá usar {n_latas18} latas de 18 litros e mais {num_galao} galões de 3.6 litros,'
        f'no valor de R$ {val_total}')
