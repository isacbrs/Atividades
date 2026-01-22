opcao = input("Qual é o tipo da sua parede? (1)Quadrada ou Retangular, (2)triangular ou (3)Circular:")

if opcao==str(1):
    l = float(input("Qual é a Base da sua parede em metros:"))
    a = float(input("Qual é a Altura da sua parede em metros:"))
    a1= float(l)*float(a)
    t1= float(a1)/int(2)
    print('A área da sua parede é de:{}metros quadrados, então é necessário {}litros de tinta para pintá-la'. format(a1, t1))
if opcao==str(2):
    b= float(input("Qual é a Base da sua parede em metros:"))
    h= float(input("Qual é a Altura da sua parede em metros:"))  
    a2= float(b)*float(h)/2 
    t2= float(a2)/int(2)
    print('A área da sua parede é de:{}metros quadrados, então é necessário {}litros de tinta para pintá-la'. format(a2, t2))
if opcao==str(3):
    r= float(input("Qual é o Raio da sua parede em metros:"))
    p= float(3.14)
    a3= float(r)**int(2)*float(p)
    t3= float(a3)/int(2)
    print('A área da sua parede é de:{}metros quadrados, então é necessário {}litros de tinta para pintá-la'. format(a3, t3))

