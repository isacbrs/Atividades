import random
n = int(random.choice([0,1,2,3,4,5]))
p = int(input("Adivinhe o número que estou pensando(de 1 á 5):"))
if p == n:
    print("Parabéns! Você acertou!")
else:
    print("Você errou! Eu estava pensando no número", n)    
