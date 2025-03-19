import math
try:
    raio = float(input('Insira o valor do raio(m): '))
    area = 4 * math.pi * raio ** 2
    volume = (4/3) * math.pi * raio ** 3
    print(f'A área da esfera é {area: .2f}(m²) e o volume é {volume: .2f}(m³)')
except:
    print('ERRO: Dados de entrada')