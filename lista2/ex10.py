try:
    q = 0
    soma = 0
    x = int(input('Digite um número inteiro e positivo: '))
    intervalo_inf = 6
    intervalor_sup = 6 * x
    if(x < 0):
        print('Número inválido')
    for i in range(intervalo_inf, intervalor_sup + 1):
        if(i % 6 == 0):
            q += 1
            soma += i
    media = soma / q
    print(f"A média dos números múltiplos de 6 entre {intervalo_inf} e {intervalor_sup} é: {media}")
        
except Exception as e:
    print(f'Erro: {e}')