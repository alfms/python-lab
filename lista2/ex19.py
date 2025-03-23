try:
    for n in range(1000, 1500 + 1):
        if(n % 7 == 0 or n % 13 == 0):
            print(n)

except Exception as e:
    print(f"ERRO: {e}")