#TRATAMENTO DE EXCECAO
try:
    #DEFINIÇÃO DE VARIÁVEIS
    mix1 = 0
    mix2 = 0
    mix3 = 0
    total_votos = 0

    #ENTRADA
    while True:
        voto = int(input("Qual Mix você mais gostou? Digite (1 - Mix 1, 2 - Mix 2, 3 - Mix 3): "))
        if(voto == 1):
            mix1 += 1
            total_votos += 1
        elif(voto == 2):
            mix2 += 1
            total_votos += 1
        elif(voto == 3):
            mix3 += 1
            total_votos += 1
        elif(voto == 0):
            break
        else:
            print("Opção inválida")
    #PROCESSAMENTO
    perc1 = (mix1 / total_votos) * 100
    perc2 = (mix2 / total_votos) * 100
    perc3 = (mix3 / total_votos) * 100
    #SAIDA
    print(f"Mix 1: {perc1}%")
    print(f"Mix 2: {perc2}%")
    print(f"Mix 3: {perc3}%")

except Exception as e:
    print(f"Erro: {e}")