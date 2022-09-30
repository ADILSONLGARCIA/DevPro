'''
EX 059. Faça um programa que leia 5 números e informe o maior número.
'''
num = list()

for c in range(0, 5):
    num.append(int(input('Digite um número: ')))

print(f'O maior número é: {max(num)}')
