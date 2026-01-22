s = 0
while True:
    num = int(input("Digite um número inteiro:"))
    if num == 999:
        break
    s+= num
print(f"a soma de todos os números digitados foi:{s}")