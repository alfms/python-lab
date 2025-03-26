try:
    pacientes = 0
    q = 0 
    while pacientes < 5:
        idade = int(input("Digite a idade do paciente: "))
        massa = float(input("Digite a massa do paciente: "))
        diabetes = str(input("O paciente possui diabetes? [S/N]: "))
        taxa_nd = (0.98 * massa) ** 0.5 / (1.08 * idade) 
        taxa_d = (massa) ** 0.5 / (0.93 * idade)
        if idade < 0 or massa < 0:
            print("Idade ou massa inválida!")
        if diabetes == "S" or "s":
            q += 1
            pacientes += 1
            taxa = taxa_d
        elif diabetes == "N" or "n":
            taxa = taxa_nd
            pacientes += 1
            q += 1
        print(f"A taxa de glicose do paciente é: {taxa:.2f}")
except Exception as e:
    print(f"ERRO: {e}")