'''
EX 149 - Jogo de Forca.
Desenvolva um jogo da forca.
O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente.
O jogador poderá errar 6 vezes antes de ser enforcado.

Nota:

Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!

Digite uma letra: O
A palavra é: _ _ _ _ O

Digite uma letra: E
A palavra é: _ E _ _ O

Digite uma letra: S
-> Você errou pela 2ª vez. Tente de novo!

'''

palavra = 'DevPro'.upper()

print('Jogo da Forca')
print('Descubra a palavra')

print('A palavra é: ', end = ' ')

for letra in palavra:
    print('_ ', end = ' ')

conjunto_letras_palavra = set(palavra)
conjunto_letras_digitadas = set()
erros = 0

while (not conjunto_letras_palavra.issubset(conjunto_letras_digitadas)) and erros < 7:

    print()
    print()
    letra_digitada = input('Digite uma letra: ').upper()
    conjunto_letras_digitadas.add(letra_digitada)

    if letra_digitada in conjunto_letras_palavra:
        print ( 'A palavra é: ', end = ' ' )
        for letra in palavra :
            if letra in conjunto_letras_digitadas:
                print(f'{letra} ', end = '')
            else:
                print('_ ', end = '')
    else:
        erros += 1
        print(f'-> ERRO {erros} de 6, Tente de novo!')
print()
print('Letras digitadas: ', conjunto_letras_digitadas)

if erros < 7:
    print('Parabéns, você ganhou!')
    print(f'A palavra é ->{palavra}<-')
else:
    print('Infelizmente você perdeu!')
    print(f'A palavra é ->{palavra}<-')
    print(f'Conjunto de letras digitadas {conjunto_letras_digitadas}')
