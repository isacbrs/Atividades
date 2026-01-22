import emoji 
n = input("Digite seu nome completo:")
ci= n.title()
v = ("Silva" in ci)
if v == True:
    print(emoji.emojize("Olha só, seu nome contém Silva! você e mais 34.030.104 milhões de pessoas tem esse sobrenome.:red_heart: silva:red_heart:"))
if v == False:
    print(emoji.emojize ("Obrigado por participar! mas você não é um Silva.:rosto_chorando_aos_berros:", language='pt'))
   