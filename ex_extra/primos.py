try:
    n = int(input("Digite um número: "))
    if n <= 1:
        print("Número não é primo.")
    else:
        is_prime = True
        for count in range(2, int(n ** 0.5) + 1):
            if n % count == 0:
                is_prime = False
                break
        if is_prime:
            print("Número é primo.")
        else:
            print("Número não é primo.")
except Exception as e:
    print(f"Erro: {e}")