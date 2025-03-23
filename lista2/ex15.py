try:
    num_total = 0
    num_positives = 0
    num_negatives = 0
    while True:
        n = float(input("Digite um número real: "))
        if(n > 0):
            num_positives += 1
            num_total += 1
        elif(n < 0):
            num_negatives += 1
            num_total += 1
        if(n == 0):
            break
    perc_positives = (num_positives / num_total) * 100
    perc_negatives = (num_negatives / num_total) * 100
    print(f"Percentual de números positivos: {perc_positives:.2f}%\nPercentual de números negativos: {perc_negatives:.2f}%")
except Exception as e:
    print(f"Erro: {e}")