
'''
EX.060 - Faça um programa que leia 5 números e
informe a soma e a média dos números.
'''

soma = 0
for C in range (1, 6):
    while True:
        try:
            soma += float(input('Informe um número: '))
            print(f'Acompanhamento da soma dos números informados é {soma}')
            break
        except ValueError:
            print('Você necessita digitar um número inteiro, por favor.')

media = soma / C
print(f'A média dos números informados é {media}')
