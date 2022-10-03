'''
E 015 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês,
sabendo-se que são descontados 11% para o Imposto de Renda,
8% para o INSS e
5% para o sindicato,
faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido.,'''
print('*'* 36)
print("        CALCULO DE SALÁRIO")
print('*'* 36)
valor_hora = float(input('Qual o valor da hora trabalhada? '))
horas_trabalhadas = float(input('Informe as horas trabalhadas:    '))
print('*'* 36)
salario_bruto = horas_trabalhadas * valor_hora
imposto = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
print(f'+ Salário Bruto   :       R$ {salario_bruto:.2f} ')
print(f'- IR (11%)        :       R$  {imposto:.2f}')
print(f'- INSS (8%)       :       R$  {inss:.2f}')
print(f'- Sindicato ( 5%) :       R$  {sindicato:.2f}')
descontos = imposto + inss + sindicato
salario_liquido = salario_bruto - descontos
print('*'* 36)
print(f'= Salário Liquido :       R$ {salario_liquido:.2f}')
print('*'* 36)
