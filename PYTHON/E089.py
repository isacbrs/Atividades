import emoji
ficha = list()
while True:
    nome = input('Nome do Aluno:')
    nota1 = float(input('1° Nota do Aluno:'))
    nota2 = float(input('2° Nota do Aluno:'))
    media = float((nota1+nota2) / 2)
    if media > 5.0 or media == 5.0:
       aprov = str('SIM')
    if media < 5.0:
       aprov = str('NÃO')   
    ficha.append([nome, [nota1, nota2], media, aprov])
    cont = input('Quer adicionar mais um Aluno? [S/N]').upper()
    if cont == str('N'):
      break
print('-='*30)
print(f"{'N°':<4}{'NOME':<10}{'MÉDIA':<8}{'APROVADO':>8}")
print('-='*30)
for i, a in enumerate(ficha):
   print(f"{i:<4}{a[0]:<10}{a[2]:<8}{a[3]:>6}")    
while True:
   print('-'*40)
   opc = int(input('Quer mostrar as notas de qual aluno?(Não quer -> 77)'))
   print('-'*35)
   if opc == 77:
      break
   if opc <= len(ficha) - 1:
      print(f'As notas de {ficha[opc][0]} são:{ficha[opc][1]}')   
print('>'*30)      
print(emoji.emojize(":red_heart: silva:red_heart:"))