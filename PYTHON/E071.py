while True:
    print("CAIXA ELETRÔNICO")
    cinquenta = vinte = dez = um = 0
    valor = int(input("Quanto você quer sacar?"))    
    if valor >= 1:
        rest = valor
        #50
        cinquenta = rest // 50
        rest = rest % 50

        #20
        vinte = rest // 20
        rest = rest % 20

        #10
        dez = rest // 10
        rest = rest % 10

        #1
        um = rest // 1

        print("Notas entregues:")
        print("de cinquenta: {} de vinte: {} de dez: {} de um: {}".format(cinquenta, vinte, dez, um))
    continuar = input('Quer sacar mais? [S/N]').upper()        
    if continuar == str('N'):
        break