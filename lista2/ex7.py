try:
    q = 0
    soma = 0
    for x in range(9, 90 + 1):
        if(x % 3 == 0 and x % 5 != 0):
            q += 1
            print(f"{q}º = {x}")
            soma += x
    print(f"Soma = {soma}")



except Exception as e:
    print(e)