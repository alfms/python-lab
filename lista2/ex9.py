try:
    q = 0
    soma = 0
    for n in range(10, 90 + 1):
        n = int(input("Digite um número: "))

        if(n % 5 == 2 and 9 < n < 91):
            q += 1
            soma += n
        elif(n == 0):
            break
    print(f"Quantidade de números válidos: {q}")
    print(f"Soma dos números válidos: {soma}")


except Exception as e:
    print(f"ERRO: {e}")