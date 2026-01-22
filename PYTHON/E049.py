print("\033[1;31m-="*20+"\033[m")
n= int(input("Digite um numero inteiro:"))
print("\033[1;31m-="*20+"\033[m")
print("TABUADA DO:", n)
print("\033[1;31m-="*20+"\033[m")
for c in range(0, 11):
    s = n * c
    print("{} X {} = {}".format(n, c, s))
print("\033[1;31m-="*20+"\033[m")