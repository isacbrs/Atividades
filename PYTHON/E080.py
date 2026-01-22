num = []
v = 10000000000
for f in range (1,6):
    n=(int(input('Digite um número inteiro:')))
    if n < v:
        num.insert(0,n)
    else:
        num.append(n)
    v = n
print(num)    