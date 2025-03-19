from datetime import datetime
try:
    format = "%H:%M"
    entrada = datetime.strptime(input("Digite a hora de entrada do veículo (HH:MM): "), format)
    saida = datetime.strptime(input("Digite a hora de saída do veículo (HH:MM): "), format)
    tempo = int((saida - entrada).total_seconds() / 60)
    valor = tempo // 30 * 2
    if(tempo < 30):
        print("Valor a ser pago: R$ 0,00")
    else:
        print(f"O tempo de permanência do veículo foi de {tempo} minutos e o valor a ser pago é de R$ {valor:.2f}")
except ValueError:
    print("ERRO: Dados de entrada")
    

