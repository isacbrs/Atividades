n = int(input("Digite um número inteiro:"))
b = int(input('''Digite qual será a base de conversão: 
              -1 para binário
              -2 para octal
              -3 para hexadecimal  
              '''))
#usei IA apartir daqui, decepção total
if b == 1:
    print(f'O número {n} em binário é {bin(n)[2:]}')
elif b == 2:                                
    print(f'O número {n} em octal é {oct(n)[2:]}')
elif b == 3:
    print(f'O número {n} em hexadecimal é {hex(n)[2:]}')
else:
    print("ERRO! escoha uma das opções")    

