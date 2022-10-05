'''
033. Faça um programa que recebe o salário de um colaborador e
o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5%
Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
'''
salario = []
indice = 1
novo_salario = 0
aumento = 0

def reajuste():
    if salario <= 280.00:
        indice = 20
        aumento = salario * indice
        novo_salario = salario + aumento
        salario.append(novo_salario)
    elif  280.01 > salario < 700.00 :
        indice = 15
        aumento = salario * indice
        novo_salario = salario + aumento
        salario.append(novo_salario)
    elif  700.01 > salario < 1500 :
        indice = 10
        aumento = salario * indice
        novo_salario = salario + aumento
        salario.append(novo_salario)


salario.append(float(input('Informe o seu salário: R$ ' )))
reajuste(salario)
print(salario)
print(indice)
print(aumento)
print(novo_salario)
