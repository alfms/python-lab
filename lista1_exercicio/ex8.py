try:
    escala = str(input("Digite a escala de entrada da temperatura (Celsius ou Fahrenheit): "))
    temp = int(input("Digite a temperatura: "))
    if(escala == "Celsius"):
        temp = 9 / 5 * temp + 32
        print(f"A temperatura em Fahrenheit é de {temp:.2f}°F")
    elif(escala == "Fahrenheit"):
        temp = 5 / 9 * (temp - 32)
        print(f"A temperatura em Celsius é de {temp:.2f}°C")
    else:
        print("ERRO: Escala inválida")
except:
    print("ERRO: Dados de entrada")
