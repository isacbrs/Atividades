par = []
impar = []
for p in range (1,8):
    num = int(input(f'Digit o {p}° número:'))
    if num % 2 ==0:
        par.append(num)
    else:
        impar.append(num) 
par.sort()
impar.sort()        
print(f"""Os valores Pares Digitados foram: {par} \n Os valores impares Digitados foram: {impar}""")           