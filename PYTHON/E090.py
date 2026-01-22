dados = {}
dados ['nome'] = input('Digite o nome do Aluno(a):')
dados ['media'] = float(input(f'Digite a média de {dados['nome']}:'))
if dados['media'] >= 7:
    dados['situação'] = str('Aprovado')
else:
    dados['situação'] = str('Reprovado')
for k, v in dados.items():
    print(f'{k} é {v}')