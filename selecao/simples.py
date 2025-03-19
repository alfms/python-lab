"""
SELEÇÃO SIMPLES: IF (SE)

if (CONDIÇÃO LÓGICA: True ou False):
  // BLOCO DE CONTROLE:
  // AÇÃO 1
  // AÇÃO 2
  // AÇÃO 3
  // AÇÃO ...
"""
try:
    # ALGORITMO = ENTRADA + PROCESSAMENTO (ULA) + SAÍDA
    preco = float (input('Preço (R$): '))
    quantidade = int(input('Quantidade (unidades):'))
    # PROCESSAMENTO (ULA)
    total = preco * quantidade
    if (total > 1000.00):
        total *= 0.97
    print(f'Total a pagar: R$ {total: .2f}')
except:
    print('ERRO: Dados de entrada')