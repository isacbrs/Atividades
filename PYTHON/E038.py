print("\033[1;31m-="*50)
print("\033[1;32mComparador de Números Inteiros.(Só falo qual é maior que qualkkkkk)\033[m")
print("\033[1;31m-=\033[m"*50)
n1 = int(input('Digite um número inteiro:'))
n2 = int(input('Digite outro número inteiro:'))
if n1 > n2:
    print("O primeiro número é maior que o segundo.")
elif n2 > n1:
    print("O segundo número é maior que o primeiro.")
elif n1 == n2:
    print("Os dois números são iguais.")
