try:
    reajuste = 0.95
    produtos = 0
    q = 0
    while produtos < 5:
        val = float(input("Digite o valor do produto: "))
        val_reajuste = val * reajuste
        dif_reajuste = val - val_reajuste
        if val > 0:
            produtos += 1
            q += 1
            if dif_reajuste > 25.50:
                val_reajuste *= 1.02
        else:
            print("Valor inválido.")
        print(f"Valor do produto {q}: {val:.2f} | Valor com reajuste: {val_reajuste:.2f}")

except Exception as e:
    print(f"ERRO: {e}")