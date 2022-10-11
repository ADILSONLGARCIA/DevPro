'''
163. Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:
Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:

* tipoCombustivel.
* valorLitro
* quantidadeCombustivel

Possua no mínimo esses métodos:

* abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
* abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
* alterarValor( ) – altera o valor do litro do combustível.
* alterarCombustivel( ) – altera o tipo do combustível.
* alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.

OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.
'''

class Bomba_de_combustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecerPorValor(self, valor:str ):
        litros_abastecidos = (valor / self.valor_litro)

    def _apresentar_abastecimento_se_possivel(self,litros_abastecidos:float,valor:float):
        if litros_abastecidos > self.quantidade_combustivel:
            print ( f'Nível de combustível inconsistente, {litros_abastecidos - self.quantidade_combustivel:.2f} litros' )
            print ( 'Por favor reabasteça a bomba o mais rapído possível ou interrompa as operações.')
        else:
            self.quantidade_combustivel -= litros_abastecidos
            print ( f'Abastecimento realizado, {litros_abastecidos:.2f} litros a um valor de R$ {valor:.2f}.' )
            print ( f'Restando no reservatório da bomba {self.quantidade_combustivel:.2f} litro de  {self.tipo_combustivel}.' )
    def abastecerPorLitro(self, litros_abastecidos: float):
        valor = litros_abastecidos * self.valor_litro
        self._apresentar_abastecimento_se_possivel(litros_abastecidos, valor)

    def adicionar_mais_combustivel_no_reservatorio(self, reabastecimento:float):
        if self.quantidade_combustivel >= 0 :
            self.quantidade_combustivel += reabastecimento
        else:
            print ( 'Ação irregular, a quantidade de combustível na bomba não pode ser negativa' )


bomba = Bomba_de_combustivel ('gasolina', 4.59, 100.0)

bomba.abastecerPorValor(50)

bomba.abastecerPorLitro(50)

bomba.valor_litros = 1,59

bomba.abastecerPorValor(50)

bomba.adicionar_mais_combustivel_no_reservatorio(100)

bomba.abastecerPorLitro(200)
