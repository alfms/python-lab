try:
    num_total = 0
    num_positives = 0
    num_negatives = 0
    soma_p = 0
    soma_n = 0
    while True:
        n = float(input("Digite um número real: "))
        if(n > 0):
            num_positives += 1
            num_total += 1
            soma_p += n
        elif(n < 0):
            num_negatives += 1
            num_total += 1
            soma_n += n
        if(n == 0):
            break
    media_positives = soma_p / num_positives
    media_negatives = soma_n / num_negatives 
    print(f"Média de números positivos: {media_positives:.2f}\nMédia de números negativos: {media_negatives:.2f}")
except Exception as e:
    print(f"Erro: {e}")