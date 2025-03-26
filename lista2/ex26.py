try:
    q = 0
    entrevistado = 0
    fundamental = 0
    medio = 0
    superior = 0
    soma_f = 0
    soma_m = 0
    soma_s = 0
    sal_f = 0
    sal_m = 0
    sal_s = 0
    while entrevistado < 10:
        salario = float(input("Digite o salário do entrevistado: "))
        escolaridade = str(input("Digite a escolaridade do entrevistado: [F/M/S]: "))
        if salario < 0:
            print("Salário inválido!")
        if escolaridade == "F":
            fundamental += 1
            q += 1
            entrevistado += 1
            sal_f += salario
        elif escolaridade == "M":
            medio += 1
            q += 1
            entrevistado += 1
            sal_m += salario
        elif escolaridade == "S":
            superior += 1
            q += 1
            entrevistado += 1
            sal_s += salario
        else:
            print("Escolaridade inválida!")
    soma_f = sal_f
    soma_m = sal_m
    soma_s = sal_s
    media_f = soma_f // fundamental 
    media_m = soma_m // medio 
    media_s = soma_s // superior
    print(f"A média salarial entre os niveis de escolaridade é:\n Fundamental: {media_f}\n Médio: {media_m}\n Superior: {media_s}")
except Exception as e:
    print(f"ERRO: {e}")