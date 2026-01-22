num =(int(input('Digite um número:')),  
      int(input('Digite outro número:')),  
      int(input('Digite mais um número:')),  
      int(input('Digite o último número:')))
if 9 in num:
  print(f'O número 9 apareceu {num.count(9)} vezes')
else:
   print('Não tem o número 9')  
if 3 in num:
  print(f'O número 3 aparece na posição: {num.index(3)+1}')
else:
   print('Não tem o númeor 3')  
print('Os números pares são:', end='')      
for n in num:
    if n % 2 == 0:    
        print(n, end='')     