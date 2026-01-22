import random
N1= input("Nome do primeiro aluno:")
N2= input("Segundo aluno:")
N3= input("Terceiro aluno:")
N4= input("Quarto aluno:")
nomes = [N1, N2, N3, N4]
#Usa random.sample para pegar uma variavel sem repitição
ordem = random.sample(nomes, k=len(nomes))
print("\nOrdem sorteada:")
print(f"O 1° aluno sorteado é: {ordem[0]}")
print(f"O 2° aluno sorteado é: {ordem[1]}")
print(f"O 3° aluno sorteado é: {ordem[2]}")
print(f"O 4° aluno sorteado é: {ordem[3]}")   