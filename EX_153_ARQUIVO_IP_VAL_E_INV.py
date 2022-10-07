"""Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo,
contendo um relatório dos endereços IP válidos e inválidos."""
# Função que para validar os Ip's
def valida_ip(ip:str) -> bool :
    numeros = ip.split('.')
# Diferente de quatro = False
    if len(numeros) != 4:
        return False
# Onúmeros devem ser entre 0 e 255 = True
    for n in numeros :
        if not (0 <= int ( n ) <= 255) :
            return False
# Se tive menos de 9 strings = False
    for n in numeros[0 :1] :
        if int ( n ) == 9 :
            return False
    return True


ips_validos = []
ips_invalidos = []
validar = []

# Lendo o arquivo txt
with open("sample_data/ip.txt", 'r') as arquivo:
    for linha in arquivo:
        ip = linha.strip()
# separando os ip's validos e invalidos em 02 listas distintas
        if valida_ip (ip):
            ips_validos.append(ip)
        else:
            ips_invalidos.append(ip)
# criando arquivo txt de Endreços validos
with open("sample_data/ip_saida.txt", 'w') as arquivo:
    arquivo.writelines(f'[Endereços Válidos!]\n')
    for ip in ips_validos:
        arquivo.writelines(f'{ip}\n')
    arquivo.writelines('\n')
    arquivo.writelines(f'[Endereços Inválidos!]\n')
    for ip in ips_invalidos:
        arquivo.writelines(f'{ip}\n')

print(ips_validos)
print(ips_invalidos)

