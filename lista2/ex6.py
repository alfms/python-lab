try:
    clientes = 0
    clienteA = 0
    clienteB = 0
    clienteC = 0
    SM = 998.05
    while(clientes < 5):
        salario = float(input("Digite o salário do cliente: "))
        if(salario < 5 * SM):
            clienteC += 1
            clientes += 1
        elif(salario < 15 * SM):
            clienteB += 1
            clientes += 1
        else:
            clienteA += 1
            clientes += 1
        
        percA = (clienteA / clientes) * 100
        percB = (clienteB / clientes) * 100
        percC = (clienteC / clientes) * 100

    print(f"Clientes A = {percA:.2f}%")
    print(f"Clientes B = {percB:.2f}%")
    print(f"Clientes C = {percC:.2f}%")
        


except Exception as e:
    print(e)