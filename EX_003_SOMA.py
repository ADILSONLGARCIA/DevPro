# 003. Faça um Programa que N números e imprima a soma.
num = num1 = 0
q = int(input('Quantos números você deseja somar: '))
for i in range(q):
    num = int(input(f'Informe o {i+1}º número: '))
    num1 += num
print(f'A soma dos números foi {num1}')
