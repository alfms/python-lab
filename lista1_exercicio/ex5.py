try:
    c = int(input('Digite o número de crianças presente: '))
    j = int(input('Digite o número de jovens presente: '))
    a18 = int(input('Digite o número de adultos que doaram um quilo de alimento presente: '))
    a = int(input('Digite o número de adultos que nao levaram alimento presente: '))
    ingresso = 150
    soma_c = c * 0
    soma_j = j * 150 * 1 / 2
    soma_a18 = a18 * 150 * 1 /2
    soma_a = a * ingresso
    publico = c + j + a18 + a
    arrecadacao = soma_c + soma_j + soma_a18 + soma_a
    print(f'O público total no jogo de futebol foram de {publico} pessoas, e a arrecadação total foi de R${arrecadacao}')
except:
    print('ERRO: Dados de entrada')