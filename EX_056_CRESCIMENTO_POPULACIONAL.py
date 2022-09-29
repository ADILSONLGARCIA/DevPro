'''
Ex 056
Supondo que a população de um país A seja da ordem de 80000 habitantes
com uma taxa anual de crescimento de 3% e que a
população de B seja 200000 habitantes com uma taxa de crescimento de 1.5%.
Faça um programa que calcule e escreva
o número de anos necessários para que a população do país A ultrapasse ou iguale
a população do país B, mantidas as taxas de crescimento.
'''

pop_A = 80_000
pop_B = 200_000
ano = 0
while pop_A < pop_B:
    pop_A += int(pop_A * .03)
    pop_B += int(pop_B * .015)
    ano += 1
print(ano, round(pop_A), round(pop_B))
