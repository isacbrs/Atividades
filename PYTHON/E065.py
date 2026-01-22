q = str("i")
soma = quant = numero1 = numero2 =0
while q != str('N'):  
 num = int(input("Digite um número:"))
 q = str(input("Quer continuar?[S/N]")).upper()
 soma+=num
 quant+= 1 
 if quant == 1:
    numero1 = numero2 = num  
 if numero1 < num:
     numero1 = num
 if numero2 > num:
     numero2 = num     
media = soma / quant
print("A média é : {}".format(int(media)))
print("O numero: {} é o maior".format(numero1))
print("O numero: {} é menor".format(numero2))