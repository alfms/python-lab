try:
    Q = 0
    num = 0
    soma = 0
    while(num < 5):
        n = float(input("Digite um número ímpar e múltiplo de 7: "))
        if(n % 2 !=0 and n % 7 == 0):
            Q += 1
            num += 1
        else:
            print("Número inválido. Tente novamente.")
        soma += n
    media = soma / Q
    print(f"A média dos números digitados é {media}")

except Exception as e:
    print(f"ERRO: {e}")