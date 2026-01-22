import random
palpite = 0
n = int(random.choice([0,1,2,3,4,5]))
while True:    
    p = int(input("Adivinhe o número que estou pensando(de 1 á 5):"))
    palpite = palpite + 1
    if p == n:
        print("Parabéns Você acertou! eu estava pensando no número:{}, você demorou somente: {} tentativas para acertar".format(n, palpite))
        break
    else:
        print("Você errou! Tente novamente")
          
