vc = int(input('Qual o valor da casa? R$:'))
sa = int(input('Qual o seu salário? R$:'))
an = int(input("Por quantos anos você vai pagar as parcelas?"))
p = vc / (an * 12)
if p > (sa * 0.3):
    print("Infelizmente seu empréstimo foi negado!, as parcelas irão passar de 30% do seu salário.")
else:
    print("PARABÉNS! Seu empréstimo foi aprovado!, aguarde o contato da nossa equipe.")
    print("Já adiantando, o valor das parcelas mensais será de R${:.2f} reias durante {} anos.".format(p, an))    