t1 = int(input("Digite sua nota no 1° trimestre:"))
t2 = int(input("Digite sua nota no 2° trimestre:"))
t3 = int(input("Digite sua nota no 3° trimestre:"))
m = float((t1 + t2 + t3) / 3)
if m < 5:
    print("\033[1;31mREPROVADO!\033[m")
elif m >= 5 and m < 7:
    print("\033[1;33mRECUPERAÇÃO!\033[m")
elif m >= 7:
    print("\033[1;32mAPROVADO!\033[m")        