"""
SELEÇÃO COMPOSTO: IF - ELSE

if (CONDIÇÃO LÓGICA):
  // BLOCO DE CONTROLE: IF
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

Operadores de valores inteiros:
-> MOD (%) : Resto inteiro da divisão.   . EXEMPLO: 7234 % 10  = 4
-> DIV (//): Quociente inteiro da divisão. EXEMPLO: 7234 // 10 = 723
"""
# TRATAMENTO DE EXCEÇÃO:
try:
    senha = int(input('Entre com uma senha numérica (4 Dígitos: XXXX): '))
    # TRATAMENTO DE ERRO:
    if (senha < 1000 or senha > 9999):
        print('ERRO: Senha inválida (deve conter 4 dígitos)')
    if(senha % 2 == 0 and senha % 17 != 0):
        print('SENHA: Criptografia forte')
    else:
        print('SENHA: Criptografia fraca')
except:
    print('ERRO: Dados de entrada')