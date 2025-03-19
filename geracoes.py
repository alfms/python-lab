"""
  SELEÇÃO ENCADEADA: IF - ELIF - ELSE

  if (CONDIÇÃO LÓGICA 1 == True):
    // BLOCO DE CONTROLE: IF
    // AÇÃO 1
    // AÇÃO 2
    // AÇÃO 3
    // AÇÃO ...
  elif (CONDIÇÃO LÓGICA 2):
    // BLOCO DE CONTROLE: ELIF
    // AÇÃO 1
    // AÇÃO 2
    // AÇÃO 3
    // AÇÃO ...
  else:
    // BLOCO DE CONTROLE: ELSE
    // AÇÃO 1
    // AÇÃO 2
    // AÇÃO 3
    // AÇÃO ...
"""
# TRATAMENTO DE EXCEÇÃO:
try:
  idade = int(input('IDADE DO ENTREVISTADO (EM ANOS): '))
# TRATAMENTO DE ERRO
  if(idade < 15):
    print('ERRO: VOCÊ ESTÁ SEM CLASSIFICAÇÃO')
  else:
    if(idade < 21):
      print('GERAÇÃO: Z')
    elif (idade < 35):
      print('GERAÇÃO: Y')
    elif (idade < 50):
      print('GERAÇÃO: X')
    elif (idade < 65):
      print('GERAÇÃO: BABY BOOMERS')
    else:
      print('GERAÇÃO: SILENCIOSA')
except:
  print('ERRO: DADOS DE ENTRADA')