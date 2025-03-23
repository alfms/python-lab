try:
    num_min = 0
    while True:
        num = float(input("Digite qualquer número real e positivo: "))
        if(num == 0):
            break
        if(num < num_min):
            num_min = num
    print(f"O menor número digitado foi {num_min}")

except Exception as e:
    print(f"ERRO: {e}")