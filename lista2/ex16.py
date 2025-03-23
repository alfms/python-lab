try:
    min_even = 0
    max_even = 0
    min_odd = 0
    max_odd = 0
    num = 0
    while(num < 10):
        n = float(input("Digite um número: "))
        if(n < 0):
            print("Número inválido, tem que ser positivo.")
        if(n % 2 == 0):
            num += 1
            if(n < min_even or min_even == 0):
                min_even = n
            elif(n > max_even):
                max_even = n
        if(n % 2 != 0):
            num += 1
            if(n < min_odd or min_odd == 0):
                min_odd = n
            elif(n > max_odd):
                max_odd = n
    print(f"Menor número par: {min_even}\n Maior número par: {max_even}")
    print(f"Menor número ímpar: {min_odd}\n Maior número ímpar: {max_odd}")
                
except Exception as e:
    print(f"ERRO: {e}")