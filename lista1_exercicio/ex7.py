try:
    preco = float(input("Digite o valor do produto a ser reajustado: "))

    while True:
        opcao = str(input("O valor de reajuste do produto será de acréscimo ou desconto (3%)?: "))
        if(opcao == "acréscimo"):
            preco *= 1.03
            print(f"O valor do produto com acréscimo de 3% é de R${preco:.2f}")
            break
        elif(opcao == "desconto"):
            preco *= 0.97
            print(f"O valor do produto com desconto de 3% é de R${preco:.2f}")
            break
        else:
            print("Opção inválida: Digite 'acréscimo' ou 'desconto'")
except:
    print("ERRO: Dados de entrada")
        
