# 013. Tendo como dado de entrada a altura (h) de uma pessoa,
# construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

sexo = input('Digite seu sexo [M/F]: ').upper()

altura_2 = float(input('Digite sua altura: '))

masculino = (72.7 * altura_2) - 58

feminino = (62.1 * altura_2) - 44.7

if sexo == 'M':
  print(f'Seu peso ideal é: {masculino:.2f}' )

elif sexo == 'F':
  print(f'Seu peso ideal é: {feminino:.2f}')
  