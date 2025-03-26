try:
    inverno = 0
    d = 0
    soma = 0
    while inverno < 90:
        temp = float(input("Digite a temperatura em graus Celsius: "))
        if(temp < -15 and temp > 5):
            print("Temperatura fora do intervalo de inverno.")
        else:
            inverno += 1
            d += 1
            soma += temp
        media = soma/d
        print(f"A média das temperaturas do inverno é: {media:.2f}°C")

except Exception as e:
    print(f"ERRO: {e}")