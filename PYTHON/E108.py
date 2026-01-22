from módulos import moeda
n = int(input('Qual é o valor?'))
print(f'aumentanod 10%¨de {moeda.moedas(n)} temos: {moeda.aumentar(n):.2f}')
print(f'diminuindo 10%¨de {moeda.moedas(n)} temos: {moeda.diminuir(n):.2f}')
print(f'O dobro de {moeda.moedas(n)} é {moeda.dobro(n)}')
print(f'A metade de {moeda.moedas(n)} é {moeda.metade(n)}')