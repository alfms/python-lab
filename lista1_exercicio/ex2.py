try:
    B = float(input('Insira o valo da Base em centímetros(cm): '))
    H = float(input('Insira o valo da Altura em centímetros(cm): '))
    if(B < 0 or H < 0):
        print('Insira valores válidos')    
    P = round(2 * (B + H), 2)
    polegadas = round(P / 2.54, 2)
    yd = round(P / 91.44, 2)
    print(f'O perímetro em centímetros é: {P} cm')
    print(f'O perímetro em polegadas é: {polegadas} pol')
    print(f'O perímetro em jardas é: {yd} yd')
except:
    print('ERRO: Dados de entrada')
    