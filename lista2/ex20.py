try:
    q = 0
    vip = 0
    std = 0
    count_vip = 0
    count_std = 0
    while True:
        salary = float(input("Digite o salário (Digite 0 para parar): "))
        if(salary == 0):
            break
        if(salary < 5000):
            q += 1
            std += 1
        else:
            q += 1
            vip += 1
    count_vip = (vip/q)*100
    count_std = (std/q)*100
    print(f"Quantidade de pessoas: {q}\nVIP: {count_vip:.2f}%\nStandard: {count_std:.2f}%")
except Exception as e:
    print(f"ERRO: {e}")