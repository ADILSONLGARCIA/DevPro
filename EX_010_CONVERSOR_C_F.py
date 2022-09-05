# 010. Faça um Programa que peça a temperatura em graus Celsius,
# transforme e mostre a temperatura em graus Fahrenheit.
# Um bisu: f = 1.8 * c + 32
print('-=' * 20)
print('CONVERSOR DE CELSIUS PARA FAHRENHEIT')
print('-=' * 20)
c = float(input('Informe a temperatura em CELSIUS[cº]: '))
f = 1.8 * c + 32
print(f'A conversão de Celsius é {c:.2f} Cº para Fahrenheit é {f:.2f} Fº')
