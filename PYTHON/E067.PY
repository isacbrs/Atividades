while True: 
  n = int(input("Digite um número inteiro: "))
  if n < 0:
    break
  else:
    print("TABUADA DO:", n)
    for c in range(0, 11):
        s = n * c
        print("{} X {} = {}".format(n, c, s))