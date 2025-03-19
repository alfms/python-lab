try:
    faltas = int(input('Digite o número de faltas: '))
    if(faltas > 10):
        print(f'Reprovado por faltas')
    else:
        AV1 = float(input('Digite a nota da AV1 [0-10]: '))
        AV2 = float(input('Digite a nota da AV2 [0-10]: '))
        MP = (AV1 + AV2) / 2
        if(MP < 3):
            print(f'Sua média foi de: {MP} - STATUS: Reprovado por nota')
        elif(MP < 7):
            print(f'Sua média foi de {MP} - STATUS: Recuperação Final')
            PF = float(input('Digite a nota da PF [0-10]: '))
            MF = (MP + PF) / 2
            if(MF < 5):
                print(f'Sua média final foi de {MF} - STATUS: Reprovado por média')
            else:
                print(f'Sua média final foi de {MF} - STATUS: Aprovado')
        else:
            print(f'Sua média foi de {MP} - STATUS: Aprovado')
except Exception as ERRO_EXCECAO:
    print(f'Erro: {ERRO_EXCECAO}')
