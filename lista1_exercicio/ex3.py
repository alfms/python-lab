try:
    segundos = float(input('Insira o tempo de permanência do aluno no Laboratório de Programação:UVV em segundos(s): '))
    horas = segundos // 3600
    segundos %= 3600
    minutos = segundos // 60
    segundos %= 60
    print(f'O aluno permaneceu no laboratório por {horas} Hora(s) + {minutos} Minutos(s) + {segundos} Segundo(s).')
except:
    print('ERRO: Dados de entrada')
