try:
    A = float(input('Digite um número A: '))
    B = float(input('Digite um número B: '))
    C = float(input('Digite um número C: '))
    # IDENTIFICAR SE É TRIÂNGULO
    if(A + B > C and A + C > B and B + C > A):
        print("Os números formam um triângulo")
        if(A == B and A == C):
            print("É um triângulo equilátero")
        elif(A == B or A == C or B == C):
            print("É um triângulo isósceles")
        else:
            print("É um triângulo escaleno")
    else:
        print("Os números não formam um triângulo")
except Exception as ERRO_EXCECAO:
    print(f"Ocorreu um erro inesperado: {ERRO_EXCECAO}")

