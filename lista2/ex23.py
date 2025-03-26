try:
    maratonista = 0
    tempo_vencedor = float("inf")
    inscVencedor = 0
    while maratonista < 20000:
        insc = int(input("Digite o número de inscrição: "))
        if insc > -1:
            maratonista += 1  
            tempo = float(input(f"Digite o tempo do maratonista {insc} (minutos): "))
            if tempo > 0 and tempo < tempo_vencedor:
                tempo_vencedor = tempo
                inscVencedor = insc
        else:
            print("Número de inscrição inválido.")
    print(f"O vencedor é o maratonista {inscVencedor} com tempo de {tempo_vencedor} minutos.")
except Exception as e:
    print(f"ERRO: {e}")