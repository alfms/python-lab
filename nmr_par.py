# EXEMPLO 1: Exibir na tela os números PARES de [0, 10].
quantidade = 0      # ENUMERAR: CONTAR 
print('NÚMEROS PARES ENTRE [0, 10] SÃO: ')
for contador  in range(11):
  if(contador % 2 == 0):
    quantidade += 1
    print(f'{quantidade}º NÚMERO PAR: {contador}')