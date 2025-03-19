"""
  EXEMPLO 7:
  Enumerar e exibir na tela os números ímpares E não múltiplos de 5 entre
  [X + Y, X ** 2 + Y ** 2]. Onde X e Y são valores >= 1 lido do usuário.
  Exibir na tela também a soma e a média deste números.

  VALOR INICIAL: X + Y
  VALOR FINAL. : X ** 2 + Y ** 2

  OBS: (X ** 2 + Y ** 2) + 1, pois o VALOR FINAL: não incluso.
"""
try:
  X = int(input('INSIRA O VALOR DE X (X >= 1): '))
  Y = int(input('INSIRA O VALOR DE Y (Y >= 1): '))
  inicial = X + Y
  final = ((X ** 2) + (Y ** 2)) + 1
  if(X < 1):
    print('O VALOR DE X DEVE SER >= 1')
  if(Y < 1):
    print('O VALOR DE Y DEVE SER >= 1')
  else:
    print(f'OS NÚMEROS ÍMPARES E NÃO MÚLTIPLOS DE 5 ENTRE [{inicial}, {final}] SÃO:')
  Q = 0
  soma = 0
  for contador in range(inicial, final):
    if(contador % 2 != 0 and contador % 5 != 0):
        Q += 1
        soma += contador
        print(f'{Q}º ÍMPAR: {contador}')
  media = soma / Q
  print(f'A SOMA DOS NÚMEROS: {soma}')
  print(f'A MÉDIA DOS NÚMEROS: {media}')
except ValueError:
   print('ERRO: INSIRA NÚMEROS VÁLIDOS') 




