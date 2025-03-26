import math
try:
    S = math.pi
    M = 1 / math.pi
    n = int(input("Digite um número: "))
    if n < 0:
        print("Número negativo, favor inserir número positivo inteiro!")
    for count in range(2, n + 1, 2):
        S += math.pi / count
    for count in range(3, n + 1, 2):
        M *= count / math.pi
    print(f"S = {S:.2f}")
    print(f"M = {M:.2f}") 

except Exception as e:
    print(f"Erro: {e}")