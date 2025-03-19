try:
    # DEFININDO VALOR DE PHI
    phi = 11.52743
    # DEFININDO VARIÁVEIS E RECEBENDO VALORES
    x = int(input("Digite um número X real qualquer: "))
    y = int(input("Digite um número Y real qualquer: "))
    z = int(input("Digite um número Z real qualquer: "))
    # CALCULANDO A MÉDIA AO CUBO DOS NÚMEROS
    media = (x + y + z) // 3
    media_cubo = media ** 3
    # DEFININDO INTERVALO
    intervalo_inferior = int(10 * phi)
    intervalo_superior = int(200 * phi)
    if(media < intervalo_inferior or media > intervalo_superior):
            print(f'O valor da média é {media_cubo} e está fora do intervalo [{intervalo_inferior}, {intervalo_superior}]')
    else:
            print(f'O valor da média é {media} e está dentro do intervalo [{intervalo_inferior}, {intervalo_superior}]')
except Exception as ERRO_EXCECAO:
    print(f'ERRO: {ERRO_EXCECAO}')
     
    
    