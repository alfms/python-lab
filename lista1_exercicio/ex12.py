try:
    massa = float(input("Qual o seu peso(Kg)?: "))
    altura = float(input("Qual a sua altura(m)?: "))

    imc = massa / (altura ** 2)

    if (imc < 18.5):
        print(f"IMC: {imc: .2f} - Magreza")
    elif (imc < 25.0):
        print(f"IMC: {imc: .2f} - Saudável")
    elif (imc < 30.0):
        print(f"IMC: {imc: .2f} - Sobrepeso")
    elif (imc < 35.0):
        print(f"IMC: {imc: .2f} - Obesidade Grau I")
    elif (imc < 40.0):
        print(f"IMC: {imc: .2f} - Obesidade Grau II (Severa)")
    else:
        print(f"IMC: {imc: .2f} - Obesidade Grau III (Mórbida)")
except:
    print("ERRO: Dados de entrada")
