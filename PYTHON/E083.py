equação = str(input('Digite uma equação com parenteses:'))
lista = []
for símb in equação:
    if símb == '(' :
        lista.append('(')
    elif símb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Os parenteses estão colocados da maneira certa!')
else:
    print('ERRADO!')