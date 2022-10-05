'''
EX 140 - Nome ao contrário em maiúsculas.
Faça um programa que permita ao usuário digitar o seu nome
e em seguida mostre o nome do usuário de trás para frente
utilizando somente letras maiúsculas.
Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.
'''

name = input('Digite seu nome: ').upper()
name2 = name.split()
a = " ".join(list(reversed(name)))
b = "  ".join(reversed(name2))
print(f' nomes com letras invertidas: {a}')
print(f'nomes invertidos {b}')
