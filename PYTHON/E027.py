import emoji
f = input("Digite seu nome completo:")
v = (f.title())
n = v.split()

if v =="Iris Fabiane Barros Silva":
    print(emoji.emojize("Oi mãe, saiba que te amo bastante, obrigado por sempre me apoiar e me ensentivar, te amo mãe:red_heart:"))
elif v =="Hellen Gomes Santana":
     print(emoji.emojize("oi ruivinha, saiba que te amo bastante, obrigado por sempre me apoiar e me ensentivar, eu te amo meu bem:red_heart:"))
elif v =="Josemir Dos Santos Silva":
     print("Oi miro, obrigado por sempre me apoiar e me ensentivar")
else:
     print("Seu primeiro nome é: {}".format(n[0]))
     print("Seu último nome é: {}".format(n[-1])) 