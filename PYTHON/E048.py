print("Contador de número ímpares múltiplos de 3 entre 1 e 500:")
s = 0
for c in range(1, 501):
    if c % 3 == 0 and c % 2 != 0:
        s += c

print("A soma total é igual a: {}".format(s))