import random
N1= input("Nome do primeiro aluno:")
N2= input("Segundo aluno:")
N3= input("Terceiro aluno:")
N4= input("Quarto aluno:")
nomes = [N1, N2, N3, N4]
print("O aluno sorteado é:{}".format(random.choice(nomes)))
#Usa random.choice para pegar uma ordem aleatoria
#Tem que ser "nomes" dentro do .format pq o comando -> -random.choice- escolhe uma variavel da lista "nomes"
#(á lista é:N1,  N2, N3, N4)