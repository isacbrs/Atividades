matriz = [[],[],[]]
for p in range (1,10):
    num = int(input(f'Digite o {p}° número inteiro:'))
    if p <=3:
        matriz[0].append(num)
    elif p > 3 and p <= 6:
        matriz[1].append(num)    
    else:
        matriz[2].append(num)   
print(f"""Á matriz é:\n{matriz[0]}\n{matriz[1]}\n{matriz[2]}""")