try:
    n1 = int(input("Digite o primeiro número inteiro: "))
    n2 = int(input("Digite o segundo número inteiro: "))
    n3 = int(input("Digite o terceiro número inteiro: "))
    n4 = int(input("Digite o quarto número inteiro: "))
    n5 = int(input("Digite o quinto número inteiro: "))
    
    if(n1 < 0 or n2 < 0 or n3 < 0 or n4 < 0 or n5 < 0):
        print("ERRO: Números negativos")
    else:
        numeros = {n1, n2, n3, n4, n5}
        if len(numeros) == 5:
            print("Os números são diferentes")
        else:
            print("Os números são iguais")
        pares = [num for num in numeros if num % 2 ==0]
        impares = [num for num in numeros if num % 2 !=0]
        if(pares):
            media_pares = sum(pares) / len(pares)
        if(impares):
            media_impares = sum(impares) / len(impares)
            print(f"Números pares: {pares}")
            print(f"Média dos números pares: {media_pares:.2f}")
            print(f"Números ímpares: {impares}")
            print(f"Média dos números ímpares: {media_impares:.2f}")
except Exception as ERRO_EXCECAO:
    print(f"Ocorreu um erro inesperado: {ERRO_EXCECAO}")

