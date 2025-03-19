try:
    Q_1 = 0
    Q_2 = 0
    soma_1 = 0
    soma_2 = 0
    p = 0
    max_h_1 = 0
    max_h_2 = 0
    soma_halto = 0
    Q_halto = 0
    while p < 50:
        sexo = int(input("Digite o seu sexo (1 - Masculino, 2 - Feminino): "))
        if(sexo != 1 and sexo != 2):
            print("Sexo inválido")
        h = float(input("Digite a sua altura em metros(m): "))
        if(h < 0):
            print("Altura inválida")
        if(sexo == 1):
            Q_1 += 1
            soma_1 += h
            p += 1
            if(h > max_h_1):
                max_h_1 = h
        elif(sexo == 2):
            Q_2 += 1
            soma_2 += h
            p += 1
            if(h > max_h_2):
                max_h_2 = h
        if(h > 1.82):
            Q_halto += 1
            soma_halto += h
    perc_halto = (Q_halto / p) * 100
    media_1 = soma_1 / Q_1
    media_2 = soma_2 / Q_2
    print(f"Média de altura dos homens: {media_1}m")
    print(f"Média de altura das mulheres: {media_2}m")
    print(f"O homem mais alto tem a altura: {max_h_1}m")
    print(f"A mulher mais alta tem a altura: {max_h_2}m")
    print(f"Percentual de pessoas com altura superior a 1,82m: {perc_halto}%")
except Exception as e:
    print(f"Erro: {e}")