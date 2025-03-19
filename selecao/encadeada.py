"""
  -> PADRÃO IF- ELIF - ELSE
  if Condição 1:
    # Bloco if
  elif Condição 2:
    # Bloco elif
  else:
    // Bloco else

  ENUNCIADO DO EXEMPLO: Notas da UVV
  Escrever um algoritmo que leia a nota [0.0, 10.0] do 1º e 2º Bimestre de um (1) aluno e
  exibir a sua média semestral (MS) com sua classificação (Status), a saber:
  -> Nota Semestral      : [0.0, 3.0[ => Aluno Status: Reprovação.
  -> Nota Semestral Final: [3.0, 7.0[ => Aluno Status: Prova Final.
      -> Ler [0.0, 10.0] a nota da Prova Final e exibir o Status:
        -> [0.0, 5.0[: Status: Reprovação.
        -> [5.0, 10.0]: Status: Aprovação.
  -> Nota Semestral Final: [7.0, 10.0] => Aluno Status: Aprovação.
"""
try:
    B1 = float (input('Nota do 1º Bimestre [0.0, 10.0]: '))
    B2 = float (input('Nota do 2º Bimestre [0.0, 10.0]: '))
    # TRATAMENTO DE ERRO
    if(B1 < 0 or B1 > 10 or B2 < 0 or B2 > 10):
        print('ERRO: Dados de entrada')
    else:
        MS = round((B1 + B2) / 2, 1)
        print(f'Média Semestral: {MS: .1f}')
        if(MS < 3.0):
            print('STATUS: Reprovação')
        elif(MS < 7.0):
            print('STATUS: Recuperação')
            PF = float (input('Nota da Prova Final [0.0, 10.0]: '))
            if (PF < 0.0 or PF > 10.0):
                print('ERRO: Dados de entrada')
            else:
                MS = round((MS + PF) / 2, 1)
                print(f'Média Semestral: {MS: .1f}')
                if(MS < 5.0):
                    print('STATUS: Reprovação')
                else:
                    print('STATUS: Aprovação')
        else:
            print('STATUS: Aprovação')
except:
    print('ERRO: Dados de entrada')