try:
    q = 0
    soma = 0
    for x in range(200, 100, -1):
        if(x % 11 == 0):
            q += 1
            soma += x
            print(f'{q}º Número: {x}')
    print(f'Soma: {soma}')
    media = soma / q
    print(f'Média: {media}')
except Exception as e:
    print(f'ERRO: {e}')