try:
    moeda = str(input("Qual a moeda que deseja converter (Real, Libra, Dolar)?: "))
    valor = float(input("Qual o valor que deseja converter?: "))
    if(moeda == "Real"):
        print(f'O valor convertido para Dolar é {valor * 0.17}')
        print(f'O valor convertido para Libra é {valor * 0.13}')
    elif(moeda == "Libra"):
        print(f'O valor convertido para Real é {valor * 7.41}')
        print(f'O valor convertido para Dolar é {valor * 1.29}')
    elif(moeda == "Dolar"):
        print(f'O valor convertido para Real é {valor * 5.75}')
        print(f'O valor convertido para Libra é {valor * 0.78}')
    else:
        print("Moeda inválida")
except:
    print("ERRO: Dados de entrada")