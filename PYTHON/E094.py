#não fiz, só copiei
galera = list()
pessoa = dict()
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome:'))
    while True:
        pessoa['sexo'] = input('Sexo[M/F]:').upper()[0]
        if pessoa['sexo'] in 'MF':      
            break
        print('ERRO!, digite M-Masculino ou F-Feminino.')
    pessoa['idade'] = int(input('Idade:')) 
    soma += pessoa['idade']
    galera.append(pessoa.copy())   
    while True:
        resp = input('Quer continuar?[S/N]').upper()[0]
        if resp in 'SN':
            break
        print('ERRO! digite S-Sim, quero continuar ou N-Não quero continuar.')
    if resp == 'N':
        break
print('-='*30)     
print(f'Ao todo temos:{len(galera)} pessoas cadastradas')
média = soma / len(galera)
print(f'A média das idades é:{média:5.2f} anos')
print(f'As mulheres cadastradas foram:',end='')
for p in galera:
    if p['sexo'] in 'Ff':   
        print(f'{p["nome"]} ', end='') 
print() 
print(f'Pessoas que estão acima da média de idade:')
for p in galera:
    if p['idade'] > média:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v};', end='')
        print()
print('<< ENCERRADO >>')