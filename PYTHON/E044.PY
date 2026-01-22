pn = float(input("Digite o preço do produto R$:"))
f = int(input('''Qual a forma de pagamento? 
        [1] à vista dinheiro/cheque
        [2] à vista cartão
        [3] 2x no cartão
        [4] 3x ou mais no cartão 
        :'''))
if f == 1:
   v = pn - (pn * 10 / 100)
   print("O preço final ávista é de R${:.2f} reais".format(v))
if f == 2:
    v = pn - (pn * 5 / 100)
    print("O preço final no cartão é de R${:.2f} reais".format(v))
if f == 3:
    v = pn / 2
    print("O preço em 2x no cartão é de R$:{:.2f} reais por parcela, pagando um total de R$:{} reias".format(v, pn))    
if f == 4:
   p = int(input("Em quantas parcelas você quer dividir?"))        
   v = pn + (pn * 20 / 100)
   vp = v / p
   print("O preço em {}x  parcelas no cartão é de R$:{:.2f} reais por parcela, pagando um total de R$:{:.2f} reais".format(p, vp, v))