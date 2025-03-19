try:
    unidade = str(input("Qual a unidade de massa? (Onça(Oz), Quilograma(Kg), Tonelada(Ton)): "))
    massa = float(input("Qual a massa? "))

    if unidade == "Oz":
        oz_kg = massa * 0.02835
        oz_ton = massa * 0.00002835
        print(f"Massa em Quilogramas(Kg): {oz_kg:.2f} Kg")
        print(f"Massa em Toneladas(Ton): {oz_ton:.2f} Ton")

    elif unidade == "Kg":
        kg_oz = massa * 35.274
        kg_ton = massa / 1000
        print(f"Massa em Onças(Oz): {kg_oz:.2f} Oz")
        print(f"Massa em Toneladas(Ton): {kg_ton:.2f} Ton")

    elif unidade == "Ton":
        ton_oz = massa * 35274
        ton_kg = massa * 1000
        print(f"Massa em Onças(Oz): {ton_oz:.2f} Oz")
        print(f"Massa em Quilogramas(Kg): {ton_kg:.2f} Kg")
except:
    print("ERRO: Dados de entrada")

