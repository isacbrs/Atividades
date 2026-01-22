sexo = str(input ("Digite seu Sexo [F] ou [M]:")).upper()
while not sexo == str('M') or sexo == str('F'):
  print("ERRO! TENTE NOVAMENTE!!!")
  sexo = input ("Digite seu Sexo [F] Feminino ou [M]Masculino:").upper()
if sexo == str("M") or sexo == str("F"): 
  print("Perfeito! Bom saber")