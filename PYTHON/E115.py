pessoas = []

def leia(msg):
    while True:
        try:
            num =int(input(msg))
        except:
           print('ERRO! por favor digite um número que represente uma função válida!')
           continue
        else:
            if num == 1 or num==2 or num == 3:
                n = num
                return n 
            else:
              print('ERRO! por favor digite um número que represente uma função válida!')
              continue


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except:
        return False
    else:
        return True
    

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('ERRO!')
    else:
        print(f'Arquivo {nome} criado com sucesso') 


def lerArquivo(nome):
    dado = []
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO! não foi possível criar o arquivo!')
    else:
        for linha in a:
            dado = linha.split(':')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade = 0):
    try:
        a =open(arq, 'at')
    except:
        print('ERRO! não foi possível abrir o arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro no cadastro dos dados!')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()



#PROGRAMA PRINCIPAL:           
arq = 'cursoemvideo.txt'
if arquivoExiste(arq): 
    print('Arquivo encontrado com sucesso!')
else:
    print('Arquivo não  encontrado!')
    criarArquivo(arq)
while True:    
    print('-'*30)
    print('MENU PRINCIPAL')
    print('-'*30)
    print("""\033[33m1 - \033[34mVer pessoas cadastradas
\033[33m2 - \033[34mCadastrar uma nova pessoa
\033[33m3 - \033[31mSair do sistema\033[m""")
    ação = leia('Oque você deseja fazer?')
    if ação == 1:
        # opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    if ação == 2:
        # Opção de cadastro:
        nome = input('Nome:')
        idade = int(input('Idade:'))
        cadastrar(arq, nome, idade)
    if ação == 3:
        print('\033[31mencerrando o programa...Até logo\033[m')
        break        