try:
    quantidade = 0
    for x in range(3, 100):
        if(x % 3 == 0):
            quantidade += 1
            print(f'{quantidade}º Número: {x}')
except:
    print('ERRO: DADOS DE ENTRADA')