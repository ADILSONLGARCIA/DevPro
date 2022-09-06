# 012. Tendo como dados de entrada a altura de uma pessoa,
# construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
def peso_ideal():
        peso = float(input('Informe seu peso atual[Kg]: '))
        altura = float(input('Informe sua altura: '))
        calculo = (72.7 * altura) - 58
        print(f'Seu peso ideal é {calculo:.2f}')
        if peso > calculo:
            fora = (calculo - peso) * -1
            print(f'Você está com {fora:.2f} kilos a mais, fora de forma!')
        else:
            print('Muito bem! Você está em forma!')
        print('Fim!')


if __name__ == '__main__':
    peso_ideal()