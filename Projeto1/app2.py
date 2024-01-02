import os

restaurantes = [{'nome':'Praca', 'categoria':'Japonesa', 'ativo':False}, 
                {'nome':'Pizza Superma', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}]

def exibir_nome_programa():
    print('Sabor Expresso \n')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Alternar atividade do restaurante')
    print('4. Sair\n')

def voltar_menu():
    input('Digite alguma tecla para voltar: ')
    main()
    
def opcao_invalida():
    print('Opcao invalida!\n')
    voltar_menu()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)      
    print(texto)
    print(linha)      
    print()    
    
def cadastrar_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes!')
    nome_restaurante = input('Digite o nome do restaurante: ')
    categoria = input(f'Digitet a categoria do {nome_restaurante}: ')
    dados_restaurante = {'nome':nome_restaurante, 'categoria':categoria, 'ativo':False}    
    restaurantes.append(dados_restaurante)
    print(f'Restaurante {nome_restaurante} cadastrado!')
    voltar_menu()
    
def listar_restaurantes():
    exibir_subtitulo('Listando restaurantes!')
    print(f"{'Nome'.ljust(22)} | {'Categoria'.ljust(20)} | Status")
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        atividade_restaurante = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'-> {nome_restaurante.ljust(20)} | {categoria_restaurante.ljust(20)} | {atividade_restaurante}')
        
    voltar_menu()

def alternar_atividade_restaurante():
    exibir_subtitulo('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante a ser alterado: ')
    existencia_restaurante = False
    
    for restaurante in restaurantes:
        if(nome_restaurante == restaurante['nome']):
            existencia_restaurante = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativado!' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado! '
            print(mensagem)
    if not existencia_restaurante:
        print('O Restaurante nao foi encontrado!')
            
    voltar_menu()
    
def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        match opcao_escolhida:
            case 1:
                cadastrar_restaurante()
            case 2:
                listar_restaurantes()
            case 3:
                alternar_atividade_restaurante()
            case 4:
                print('Finalizar app!!!')
            case _:
                opcao_invalida()
    except:
        opcao_invalida()
        
def finalizar():
    exibir_subtitulo('Finalizar app!')
    
def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()
    
if __name__ == '__main__':
    main()