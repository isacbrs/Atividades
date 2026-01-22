numero1 = int(input("Digite um número:"))
numero2 = int(input("Digite outro número:"))
while True:
    e = int(input("""                   \033[1;34mMENU\033[m
            Oque você deseja fazer?
    [1]somar                    
    [2]multiplicar                   
    [3]dizer qual é maior e menor
    [4]Escolher novos números
    6 - fatorial              
    [5]\033[1;31mSAIR\033[m                                    
    :"""))
    if e == 1:
        r = numero1 + numero2
        print("{} + {} = {}".format(numero1, numero2, r)) 
    elif e == 2:
        re = numero1 * numero2
        print("{} X {} = {}".format(numero1, numero2, re))  
    elif e == 3:
        if numero1 > numero2:
            print("O {} é maior que o {}".format(numero1, numero2))
        elif numero1 < numero2:
            print("O {} é maior que o {}".format(numero2, numero1))
        else:
            print("São iguais")       
    elif e == 4:
        numero1 = int(input("Digite um número:"))
        numero2 = int(input("Digite outro número:"))       
    elif e == 5:
        print("Até a próxima!")
        break   
    elif e == 6:
        r1 = 0
        s = (numero1 - 1)
        r = numero1 * s
        r1 += r 
        if s == 1: 
            print("O resultado de {}! é : {}".format(numero1, r1))                  
    else:
        print('ERRO! TENTE NOVAMENTE')