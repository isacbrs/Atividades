def leiaint(msg):
    while True:
        try:
            n =int(input(msg))
        except:
           print('ERRO! por favor digite um número inteiro válido!')
           continue
        else:
            return n
        

def leiafloat(msg):
    while True:
        try:
            n =float(input(msg))
        except:
           print('ERRO! por favor digite um número float válido!')
           continue
        else:
            return n


num = leiaint('Digite um número inteiro:')
print(f'O valor digitado foi: {num}')
n = leiafloat('Digite um número float:')
print(f'O valor digitado foi {n}')
