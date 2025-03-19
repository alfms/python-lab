try:
    verao = 0
    d = 0
    soma = 0
    while verao < 90:
        temp = float(input("Digite a temperatura em graus Celsius: "))
        if(temp < 28):
            print("Temperatura fora do intervalo de verão.")
        else:
            verao += 1
            d += 1
            soma += temp
    media = soma/d
    print(f"A média das temperaturas do verão é: {media:.2f}°C")

except Exception as e:
    print(f"ERRO: {e}")