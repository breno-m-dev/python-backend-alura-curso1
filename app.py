from colorama import init, Fore, Style
init(autoreset=True)

import os


restaurantes = []

def pausar():
    input('\nAperte qualquer tecla para continuar ')

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear') #limpa a tela do terminal, indepentente se for windows, mac ou linux

def mostra_subtitulo(texto):
    print( Style.BRIGHT + Fore.LIGHTMAGENTA_EX  + texto +'\n')


def finalizar_app():
    limpar_tela()
    mostra_subtitulo('Encerrando o programa')

def cadastrar_restaurante():
    limpar_tela()
    mostra_subtitulo('Cadastro de novos restaurantes')
    
    nome_restaurante = input('Digite o nome do restaurante: ')
    restaurantes.append(nome_restaurante)
    
    print(Style.BRIGHT + Fore.GREEN + f'O restaurante {nome_restaurante} foi cadastrado com sucesso!\n')
    pausar()


def listar_restaurantes():
    limpar_tela()
    mostra_subtitulo('Lista de restaurantes')
    
    for restaurante in restaurantes:
        print(f'- {restaurante}')
    
    pausar()


def ativar_restaurante():
    print( Style.BRIGHT + Fore.LIGHTMAGENTA_EX  + 'Ativar restaurante\n' )

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
    print('2. Listar restaurante')
    print('3. Ativar restaurante') #o restaurante nao é mostrado no app ao ser cadastrado, precisa de confirmação antes
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
                ativar_restaurante()
                
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


 