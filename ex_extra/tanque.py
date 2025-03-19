try:
    largura = float(input('Largura em metros: '))
    altura = float(input('Altura em metros: '))
    profundidade = float(input('Profundidade em metros: '))
    tanque = largura * altura * profundidade
    volume_tanque = tanque * 1000
    valor_alcool = float(input('Valor do litro do álcool: '))
    valor_gasolina = float(input('Valor do litro da gasolina: '))
    val_tanque_alcool = volume_tanque * valor_alcool
    val_tanque_gasolina = volume_tanque * valor_gasolina
    val_20 = val_tanque_alcool * 0.2
    val_80 = val_tanque_gasolina * 0.8
    val_tanque_20_80 = val_20 + val_80
    print(f'O volume do tanque é de {volume_tanque:.2f} litros')
    print(f'O valor do tanque cheio de álcool é de R$ {val_tanque_alcool: .2f}')
    print(f'O valor do tanque cheio de gasolina é de R$ {val_tanque_gasolina: .2f}')
    print(f'O valor do tanque com 20% de álcool e 80% de gasolina é de R$ {val_tanque_20_80: .2f}')
except:
    print('ERRO: Dados de entrada')
    
