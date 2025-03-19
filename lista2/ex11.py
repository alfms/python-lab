try:
    # Inserir o número inteiro
    n = int(input("Digite um número inteiro: "))
    # Verificar se é válido
    if(n < 0):
        print("Número inválido")
    else:
        for i in range(n, n + 50):
            print(i)


except Exception as e:
    print(f'Erro: {e}')