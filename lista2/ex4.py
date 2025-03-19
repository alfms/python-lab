try:
    soma_pares = 0
    soma_impares = 0

    for i in range(10, 99 + 1):
        if(i % 2 == 0):
            soma_pares += i
        else:
            soma_impares += i
    print(f'Soma dos pares: {soma_pares}')
    print(f'Soma dos ímpares: {soma_impares}')
        
except Exception as e:
    print(f'ERRO: {e}')
            