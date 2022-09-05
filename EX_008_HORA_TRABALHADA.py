# 008. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.
print('-=' *  30)
print('CALCULO DE HORAS TRABALHADAS')
print('-=' *  30)
valor_hora = float(input('Informe, qual o valor da hora trabalhada R$: '))
horas_trabalhadas = float(input('Informe, quantas horas foram trabalhadas: '))
salario = valor_hora * horas_trabalhadas
#print(f'O salário, conforme o apontamento de horas deste mês é R${salario}' )
if __name__ == '__main__':
    print ( f'O salário, conforme o apontamento de horas deste mês é R$ {salario:.2f}' )