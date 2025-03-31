# %%
import pandas as pd

biblioteca = {
    'Titulo': [],
    'Autor': [],
    'Ano de Publicacao' : [],
    'Status' : [],
    'Responsavel' : []
}

# df = pd.DataFrame(data = biblioteca) ###USAR NO MOMENTO EM QUE QUISER EXCEL###

# %%
def add_livro():
    print('===' * 10)
    print('Para adicionar um livro, preciso que informe os seguintes dados:')

    while True:    
        titulo = input('Titulo do livro:').title().strip()
        confirma_titulo = input('Confirme o titulo do livro: ').title().strip()

        if titulo == confirma_titulo:
            biblioteca['Titulo'].append(titulo)
            break
        else:
            print('Os titulos nao identicos.Tente novamente!')

    while True:    
        autor = input('Autor do livro:').title().strip()
        confirma_autor = input('Confirme o nome do autor: ').title().strip()

        if autor == confirma_autor:
            biblioteca['Autor'].append(autor)
            break
        else:
            print('Os nomes nao sao identicos. Tente novamente!')

    while True:        
        ano_publicacao = input('Ano de publicacao do livro: ')
        confirma_anoPublicacao = input('Confirme o ano de publicacao: ')

        if ano_publicacao.isnumeric():
            if ano_publicacao == confirma_anoPublicacao:
                biblioteca['Ano de Publicacao'].append(ano_publicacao)
   
                break 
            else:
                print('Os anos nao sao identicos. Tente novamente!')
        else:
            print('Informe apenas o ano de publicacao do livro.')    
    
    print('===' * 10)

    biblioteca['Status'].append('Disponivel')
    biblioteca['Responsavel'].append('-')

    print(pd.DataFrame(data = biblioteca, index = None))
    return menu()


# %%

def listar_livros():
    return pd.DataFrame(data = biblioteca['Titulo'], index = None)


# %%
def pesquisar_livros():
    while True:
        pesquisa = input('Informe o nome do Autor/Livro que procura: ')
        confirmar_pesquisa = input('Confirme o nome do autor/livro: ')

        if pesquisa == confirmar_pesquisa:
            if pesquisa in biblioteca['Titulo']:

                for i in range(len(biblioteca['Titulo'])):
                    if biblioteca['Titulo'][i] == pesquisa:
                        print(f'Titulo: {biblioteca['Titulo'][i]}\nAutor: {biblioteca['Autor'][i]}\nAno de Publicacao: {biblioteca['Ano de Publicacao'][i]}')
            
            elif pesquisa in biblioteca['Autor']:
                
                for i in range(len(biblioteca['Autor'])):
                    if biblioteca['Autor'][i] == pesquisa:
                        print(f'Titulo:{biblioteca['Titulo'][i]}\nAutor: {biblioteca['Autor'][i]},\nAno de Publicacao: {biblioteca['Ano de Publicacao'][i]}')

            else:
                print('Autor/Livro nao encontrados na biblioteca.')
        else:
            print('Autor/Livro nao sao identicos. Tente novamente!')

#%%
#  
def emprestimo():
    if len(biblioteca['Titulo']) == 0:
        print('Nao ha livros na biblioteca.')
        return menu()

    else:
        print('Todos os titulos presentes em nossa biblioteca:')
        
        print('---' * 10)
        print(biblioteca['Titulo'],biblioteca['Status'])
        print('---' * 10)

        while True:
            livro_emprestimo = input('Informe o Titulo do livro que deseja: ').title().strip()
            resoponsavel_livro = input('Informe o nome da pessoa que sera responsavel pelo livro: ').title().strip()
            confirma_resoponsavel = input('Confirme o nome da pessoa que sera responsavel pelo livro: ').title().strip()

            if resoponsavel_livro == confirma_resoponsavel:
                if livro_emprestimo in biblioteca['Titulo']:
                    for i in range(len(biblioteca['Titulo'])):

                        if livro_emprestimo in biblioteca['Titulo']:
                            biblioteca['Status'][i] = 'Emprestado'
                            biblioteca['Responsavel'][i] = resoponsavel_livro

                            print(f'Status do {biblioteca['Titulo'][i] } alterado para {biblioteca["Status"][i]}.')
                            print(f'Responsavel pelo livro: {biblioteca["Responsavel"][i]}')
                            
                            return menu()
                        
                else:
                    print('Livro nao encontrado.')
                    return menu()
            else: 
                print('Os nomes nao sao identicos. Tente novamente!')
                

# %%
def devolucao_livro():
    status_devolvido = False
    while True:
        livro_emprestado = input('Informe o Titulo do Livro que foi emprestado: ')

        if livro_emprestado in biblioteca['Titulo']:
            
            while True:
                resoponsavel_livro = input('Informe o nome do responsavel pelo livro: ')

                if resoponsavel_livro in biblioteca['Responsavel']:

                    for i in range(len(biblioteca['Responsavel'])):
                        if biblioteca['Responsavel'][i] == resoponsavel_livro:
                            biblioteca['Status'][i] = 'Disponivel'
                            biblioteca['Responsavel'][i] = '-'

                            status_devolvido = True
                            print('Livro disponivel para emprestimo novamente.')
                            break
                else:
                    print('Responsavel nao encontrado na nossa base de dados. Tente novamente!')
        
        elif status_devolvido == True:
            break

        else:
            print('Titulo nao encontrado na nossa base de dados. Tente novamente!')
        
# %%
def menu():
    print('-=-' * 10)
    print('Informe a opcao desejada.')
 
    escolha_menu = input('''
    1 - Adicionar Livro
    2 - Listar Livros
    3 - Pesquisar Livros
    4 - Emprestimo de Livro
    5 - Devolucao de Livro
    0 - Sair
    Opcao escolhida: ''')
    print('-=-' * 10)

    if escolha_menu == '1':
        return add_livro()
    
    elif escolha_menu == '2':
        return listar_livros()
    
    elif escolha_menu == '3':
        return pesquisar_livros()
    
    elif escolha_menu == '4':
        return emprestimo()
    
    elif escolha_menu == '5':
        return devolucao_livro()
    
    elif escolha_menu == '0':
        print('Sistema Biblioteca encerrado.')
        pass

menu()


# %%
