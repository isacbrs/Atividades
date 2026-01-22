a = int(input("Digite seu ano de nascimento:"))
n = 2025 - a
if n < 18:
    print("Você ainda não deve se alistar, falta {} anos.".format(18-n))
elif n == 18:
    print("Você deve se alistar esse ano!")
elif n > 18:
    print("Já passou do tempo de alistamento, você deveria ter se alistado há {} anos atrás.".format(n-18))