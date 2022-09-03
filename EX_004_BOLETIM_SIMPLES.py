# 004. Faça um Programa que peça as 4 notas bimestrais e mostre a média.
soma_notas = 0
aluno = str(input('Por favor, informe o nome do aluno: '))
for i in range(4):
    nota = int(input(f'Informe o {i+1}º nota: '))
    soma_notas += nota
media = soma_notas / 4
print(f'A média do aluno {aluno} é {media}')
