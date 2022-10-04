salarios = [200, 250, 320, 413, 516, 680, 791, 877, 999, 1000, 2000, 3000]
contagem_de_faixa_salarial = [0] * 9
for salario in salarios:
    indice = salario // 100 -2
    indice_maximo = len( contagem_de_faixa_salarial ) - 1
    indice = min(indice, indice_maximo)
    contagem_de_faixa_salarial[indice] += 1

print(salarios)
print( contagem_de_faixa_salarial )
