try:
    num = int(input('Insira um número positivo: '))
    if(num < 0):
        print('Insira um valor válido (acima de 0).')
    quadrado = num ** 2
    if(quadrado % 2 != 0 and quadrado % 11 == 0):
        print(f'O número {quadrado} é ímpar e múltiplo de 11!')
    else:
        print(f'O número {quadrado} não é múltiplo de 11')
except: 
    print('ERRO: Dados de entrada')