'''EX_155_a. Classe Bola: Crie uma classe que modele uma bola:

Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor

EX_155_b Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

EX_155_c 155Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;

Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local.
Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
'''
# EX_155_a - Classe Bola: Crie uma classe que modele uma bola:
# Atributos: Cor, circunferência, material. E Métodos: trocaCor e mostraCorExercício 155 - a - Classe bola

class ClasseBola:
    def __init__(self):
        self.cor = 'Azul'
        self.circunferencia = 4
        self.material = 'Papel'

    def Mostra_cor(self):
        return id(self)

    def Troca_cor(self, cor):
        self.cor = cor


circulo_primeiro = ClasseBola()
circulo_segundo = ClasseBola()
print(type(circulo_primeiro))
print(circulo_primeiro is circulo_segundo)
print(id(circulo_primeiro), circulo_primeiro.Mostra_cor())
print(id(circulo_segundo), circulo_segundo.Mostra_cor())
print(circulo_primeiro.cor, circulo_segundo.cor)
print('\n')

# EX_155_b Classe Quadrado: Crie uma classe que modele um quadrado:
# Atributos: Tamanho do lado. E Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:
    def __init__(self):
        self.cor = 'Vermelho'
        self.valor_lado = 10

    def mudar_valor_lado(self, valor_lado):
        self.valor_lado = valor_lado

    def calcular_area(self, valor_lado):
        area= (self.valor_lado)**2
        return area
quadrado_x = Quadrado()

print('Primeiro Valor do QUadrado X: ',end=' ')
print(quadrado_x.valor_lado)
print(f'Novo valor do lado: ',end=' ')
quadrado_x.mudar_valor_lado(12)
print(quadrado_x.valor_lado)
print(f'Valor da Área: ',end=' ')
print(quadrado_x.calcular_area(12))

'''
 EX_155_c classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;

Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local.
Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
'''

class Retangulo():
    def __init__(self):
        self.comprimento= 10
        self.largura = 5

    def mudar_valor_dos_lados(self, comprimento, largura):
        self.largura = largura
        self.comprimento = comprimento

    def retornar_valor_dos_lados(self):
        print(self)

    def calcular_area_retangulo(self, comprimento, largura):
        area_retangulo = (self.comprimento) * (self.largura)
        return area_retangulo

    def calcular_perimetro_retangulo(self, comprimento, largura):
        perimetro_retangulo = ((self.comprimento)*2) + ((self.largura)*2)
        return perimetro_retangulo
