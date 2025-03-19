try:
    n = int(input("Digite um número inteiro >= 2: "))
    l_inferior = int(input("Digite o limite inferior: "))
    l_superior = int(input("Digite o limite superior: "))

    if(n < 2 or l_inferior > l_superior):
        print('Valores inválidos')
    else:
        print(f'Os múltiplos de {n} entre {l_inferior} e {l_superior} são: ')
        for x in range(l_inferior, l_superior + 1):
            if(x % n == 0):
                print(x)
except Exception as e:
    print(f'ERRO: {e}')


    