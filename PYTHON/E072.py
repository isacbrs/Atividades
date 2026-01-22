cont = ('zero', 'um' , 'dois' , 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 
        'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte' )
while True:
  jogador = int(input('Digite um número de 0 a 20:'))
  if 0<=jogador<=20:
    break
  else:
   print('ERRO!')
print(f'você digitou o número: {cont[jogador]}')  