s = 0
print("\033[1;31m-="*20+"\033[m")
print("Soma de números inteiros \033[1;32mPARES\033[m")
print("\033[1;31m-="*20+"\033[m")
for c in range(0,6):
    c = int(input("Digite um número inteiro:"))
    if c % 2 == 0:
        v = c
        s += v
print("A soma dos números inteiros \033[1;32mPARES\033[m enviados é igual a:", s)