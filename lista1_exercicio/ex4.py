try:
    h = float(input('Insira a sua altura em metros(m): '))
    s = str(input('Insira o seu sexo (M/F): '))
    if(s == 'M'):
        peso = round((72.7 * h) - 58, 2)
    elif(s == 'F'):
        peso = round((62.1 * h) - 44.7, 2)
    else:
        print('Sexo inválido')
    print(f'O seu peso ideal é {peso} kg.')
except:
    print('ERRO: Dados de entrada')