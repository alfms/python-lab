import math

try:
    q = 0
    soma = 0
    lim_inf = int(10 * math.pi ** 3)
    lim_sup = int(100 * math.pi)
    
    while True:
        n = float(input(f"Digite um número dentro do intervalo [{lim_inf}, {lim_sup}]: "))
        if(n > lim_inf and n < lim_sup):
            q += 1
            soma += n
        else:
            break        
    media = soma / q
    print(f"A média dos números digitados é: {media}")

except Exception as e:
    print(f"ERRO: {e}")