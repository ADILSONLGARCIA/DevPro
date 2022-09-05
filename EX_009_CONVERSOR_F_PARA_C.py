# 009. Faça um Programa que peça a temperatura em graus Fahrenheit,
# transforme e mostre a temperatura em graus Celsius.
# Um bisu: C = 5 * ((F-32) / 9).
print('-=' * 20)
print('CONVERSOR DE FAHRENHEIT PARA CELSIUS')
print('-=' * 20)
fah = float(input('Informe a temperatura em fahrenheit[Fº]: '))
c = 5 * ((fah-32) / 9)
print(f'A conversão de Fahrenheit, {fah:.2f} Fº para Celsius é {c:.2f} Cº')
