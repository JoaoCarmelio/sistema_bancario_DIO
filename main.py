menu = ''' ===== MENU =====
           [A] - DEPOSITAR 
           [B] - SACAR
           [C] - EXTRATO
           [D] - SAIR
     => '''
saldo = 0
limite = 500
extrato = ''
numero_saque = 0
LIMITE_SAQUE = 3

while True:
 op = input(menu)
   
 if op == 'a':
    print('TELA - - - DEPOSITAR') 
    valor = int(input('digite o valor desejado: \n'))
   
    if valor > 0 :
       saldo += valor
       print(f'saldo atualizado: {saldo}\n')
       extrato += f'deposito : {valor:2f}\n'
    else:
       print('Não é aceitável valores zeros ou negativos\n')
  
     
 elif op == 'b':
    print('TELA DE SAQUE\n')
    valor = int(input('digite o valor do saque:  \n'))
    # verificações
    acima_saldo = valor > saldo 
    acima_limite = valor > limite
    acima_limite_saque = numero_saque >= LIMITE_SAQUE
    
    if acima_saldo:
       print('Negado! saldo insuficiente!!')
    elif acima_limite:
       print('Negado! limite permitido ate R$500!')
    elif acima_limite_saque:
       print('Negado! só pode sacar 3 vezes!')
    elif valor > 0:
       saldo -= valor
       extrato = f'Saque : R${valor:.2f}\n'
       numero_saque =+ 1
    else:
      print('Negado! valor informado invalido!\n ')
      
 elif op == 'c':
    print('=============== EXTRATO ============')
    print('nao foram realizada moviemntações.' if not extrato else extrato)
    print(f'saldo : R${saldo:.2f}')
    print('=============== EXTRATO ==============')
   
 elif op == 'd':
   print('saindo...')
 else:
  print('informe a opção desejada novamente')
   
      
    
    