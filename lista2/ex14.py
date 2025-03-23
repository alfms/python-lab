try:
    candidato_1 = 0
    candidato_2 = 0
    nulo = 0
    eleitores = 0
    while(eleitores < 50):
        voto = int(input("1 - Candidato 1\n2 - Candidato 2\n0 - Voto nulo\nDigite seu voto para síndico: "))
        if(voto == 1):
            candidato_1 += 1
            eleitores += 1
        elif(voto == 2):
            candidato_2 += 1
            eleitores += 1
        elif(voto == 0):
            nulo += 1
            eleitores += 1
        else:
            print("Voto inválido.")
            if(candidato_1 > candidato_2):
                print("Parabéns ao candidato 1, eleito síndico do prédio.")
            elif(candidato_2 > candidato_1):
                print("Parabéns ao candidato 2, eleito síndico do prédio.")
            else:
                print("Houve empate, será necessário um novo pleito.")
    perc_1 = (candidato_1/eleitores)*100
    perc_2 = (candidato_2/eleitores)*100
    perc_nulo = (nulo/eleitores)*100
    print(f"Votos para o candidato 1: {perc_1}%\n Votos para o candidato 2: {perc_2}%\n Votos nulos: {perc_nulo}%")
except Exception as e:
    print(f"Erro: {e}")