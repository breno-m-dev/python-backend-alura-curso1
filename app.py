from colorama import init, Fore, Style
init(autoreset=True)

import os


restaurantes = [ {'nome':'Praça' , 'categoria':'Japonesa', 'ativo': False},
                 {'nome':'TOP PIZZA' , 'categoria':'Italiana', 'ativo': True},
                 {'nome':'Siri Cascudo', 'categoria':'Frutos do Mar', 'ativo': False}
]

def pausar():
    input('\nAperte qualquer tecla para continuar ')

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear') #limpa a tela do terminal, indepentente se for windows, mac ou linux

def mostra_subtitulo(texto):
    linha = '*' * ( len(texto) )

    print(linha)
    print( Style.BRIGHT + Fore.LIGHTMAGENTA_EX  + texto +'\n')
    print(linha)


def finalizar_app():
    limpar_tela()
    mostra_subtitulo('Encerrando o programa')

def cadastrar_restaurante():
    limpar_tela()
    mostra_subtitulo('Cadastro de novos restaurantes')
    
    
    nome_restaurante = input('Digite o nome do restaurante: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_restaurante}: ')

    restaurante = {'nome': nome_restaurante,
                   'categoria': categoria,
                   'ativo': False}
    
    restaurantes.append(restaurante)
    
    print(Style.BRIGHT + Fore.GREEN + f'O restaurante {nome_restaurante} foi cadastrado com sucesso!\n')
    pausar()


def listar_restaurantes():

    
    limpar_tela()
    mostra_subtitulo('Lista de restaurantes')
    
    print(f'- {'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | Estado')

    for restaurante in restaurantes:
        ativo ='ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {restaurante['nome'].ljust(20)} | {restaurante['categoria'].ljust(20)} | {ativo}')
    
    pausar()


def alterar_estado_restaurante():
    limpar_tela()
    mostra_subtitulo('Alterar estado de restaurante')
    
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False
    
    for restaurante in restaurantes:
        if restaurante['nome'] == nome_restaurante:
            restaurante['ativo'] = not restaurante['ativo']
            restaurante_encontrado = True
            break
    
    if restaurante_encontrado:
        if restaurante['ativo']:
            print(f'O estado do restaurante {nome_restaurante} foi ativado')
        else:
            print(f'O estado do restaurante {nome_restaurante} foi desativado')

    else:
        print('Restaurante não encontrado')


    pausar()
        


def exibir_nome():
    print(
        Style.BRIGHT + Fore.LIGHTRED_EX + 
        '''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░\n''' + Style.RESET_ALL)

def exibir_menu(): 
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar ou desativar restaurante') #o restaurante nao é mostrado no app ao ser cadastrado, precisa de confirmação antes
    print('4. Sair\n')

def erro_input_menu():
    print('Digite um valor válido!\n')
    pausar( )


def escolher_opcao_menu():
    # opcao_escolhida = input('Escolha uma opção')# nesse caso opcao_escolhida será uma str. Por isso ela não podera ser comparada com um int por exemplo.
    while True:
        limpar_tela()
        exibir_nome()
        exibir_menu()
        try:
            # O int() tenta converter o input em inteiro, se algo como um float ou string não numérico forem digitados, ocorre um erro no python! 
            # O try e except lidam com o erro
            opcao_escolhida = int (input(Style.BRIGHT + Fore.LIGHTCYAN_EX + 'Escolha uma opção\n' + Style.RESET_ALL))#aqui há a conversão de str para int antes de associar esse valor a variável.
            
            if opcao_escolhida == 1:  
                cadastrar_restaurante()
                
            elif opcao_escolhida == 2: 
                listar_restaurantes()
                
            elif opcao_escolhida == 3: 
                alterar_estado_restaurante()
                
            elif opcao_escolhida == 4:
                finalizar_app()
                break
            else:
                erro_input_menu()
                continue

        except ValueError:
            # Captura os erros na conversão do input para inteiro
            erro_input_menu()
    

def main():
    #par_ou_impar()

    escolher_opcao_menu()




if __name__ == '__main__':
    main()


 