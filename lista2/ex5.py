try:
    habitantes = 0
    empregados = 0
    desempregados = 0
    while habitantes < 10000:
        voto = int(input("Você está empregado? (1 - Sim, 0 - Não): "))
        if(voto == 1):
            habitantes += 1
            empregados += 1
        elif(voto == 0):
            habitantes += 1
            desempregados += 1
        else:
            print("Valor inválido. Digite 1 ou 0.")

    perc_emp = (empregados / habitantes) * 100
    perc_des = (desempregados / habitantes) * 100

    print(f"Empregados: {perc_emp}%")
    print(f"Desempregados: {perc_des}%")
except Exception as e:
    print(e)