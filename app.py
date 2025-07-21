from colorama import init, Fore, Style
init(autoreset=True)

import os;



def finalizar_app():
    os.system('cls') #limpa a tela do terminal
    print( Style.BRIGHT + Fore.LIGHTMAGENTA_EX  + 'Encerrando o programa\n' )

def cadastrar_restaurante():
    print(  Style.BRIGHT + Fore.LIGHTMAGENTA_EX + 'Cadastrar restaurante\n' )

def listar_restaurantes():
    print( Style.BRIGHT + Fore.LIGHTMAGENTA_EX  + 'Lista de restaurantes\n' )

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

def escolher_opcao_menu():
    # opcao_escolhida = input('Escolha uma opção')# nesse caso opcao_escolhida será uma str. Por isso ela não podera ser comparada com um int por exemplo.
    while True:
        try:
            # O int() tenta converter o input em inteiro, se algo como um float ou string não numérico forem digitados, ocorre um erro no python! 
            # O try e except lidam com o erro
            opcao_escolhida = int (input(Style.BRIGHT + Fore.LIGHTCYAN_EX + 'Escolha uma opção\n' + Style.RESET_ALL))#aqui há a conversão de str para int antes de associar esse valor a variável.
            if opcao_escolhida == 1:  
                cadastrar_restaurante()
                break
            elif opcao_escolhida == 2: 
                listar_restaurantes()
                break
            elif opcao_escolhida == 3: 
                ativar_restaurante()
                break
            elif opcao_escolhida == 4:
                finalizar_app()
                break
            else:
                erro_input_menu()
                continue
        except:
            # Captura os erros na conversão do input para inteiro
            erro_input_menu()
    

        


def par_ou_impar(): 
    while True:
        try:
            numero= int (input('Digite um número:\n')) 
            break
        except ValueError:
             print('Digite um valor válido!')
    
    if( numero % 2 == 0 ):
        print('numero par')
    else:
        print('numero impar')

def main():
    #par_ou_impar()
    os.system('cls')
    exibir_nome()
    exibir_menu()
    escolher_opcao_menu()




if __name__ == '__main__':
    main()


 