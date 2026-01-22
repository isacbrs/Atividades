s = float(input("Digite o seu salário R$:"))
if s > 1250:
    a = s * 10 / 100
    print("O seu aumento será de R$:{:.2f}, assim seu sálario passa a ser:{}".format(a, s + a))
elif s <= 1250:
    a2 = s * 15 / 100
    print("O seu aumento será de R$:{:.2f}, assim seu sálario passa a ser:{}".format(a2, s + a2))