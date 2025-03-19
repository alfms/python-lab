try:
    n1 = float(input('Digite qualquer número: '))
    n2 = float(input('Digite qualquer número: '))
    n3 = float(input('Digite qualquer número: '))
    n4 = float(input('Digite qualquer número: '))
    n5 = float(input('Digite qualquer número: '))
    
    numeros = [n1, n2, n3, n4, n5]
    if len(numeros) != 5:
        print("Os números são iguais")
    else:
        numeros.sort(reverse=True)
        dois_maiores = numeros[:2]
        soma_dm = sum(dois_maiores)
        media = soma_dm / 2
        print(f'A média da soma dos dois maiores números {dois_maiores[0]} e {dois_maiores[1]} é: {media:.2f}.')
except Exception as ERRO_EXCECAO:
    print(f"Ocorreu um erro inesperado: {ERRO_EXCECAO}")
