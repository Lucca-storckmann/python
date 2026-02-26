import os

restaurantes = ["Pizza", "Sushi", "Churrasco"]

def exibir_nome_programa():
    print("Sabor Express\n")

def cadastrar_novo_restaurante():
    pass

def listar_restaurantes():
    pass

def exibir_menu():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Ativar restaurante")
    print("4. Sair\n")

def cadastrar_novo_restaurante():
        os.system("cls")
        print("Cadastro de novos restaurantes")
        nome_do_restaurante = input("Digite o nome: ")
        restaurantes.append(nome_do_restaurante)
        print(f"O restaurante {nome_do_restaurante} foi cadastrado com sucesso")
        input("Digite uma tecla para retornar ao menu principal: ")
        main ()

def listar_restaurantes():
        os.system("cls")
        print("Lista de restaurantes cadastrados\n")
        for restaurantes in restaurantes:
            print(f".{restaurantes}")
        input("Digite uma tecla para retornar ao menu principal: ")
        main ()

def processar_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        print(f"Opção escolhida: {opcao_escolhida}")

        if   opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            print("Ativar restaurante selecionado.")
        elif opcao_escolhida == 4:
            print("Sair do aplicativo")
        else:
            opcao_invalida()
    except: 
        opcao_invalida()

def finalizar_app():
    os.system ("cls")
    print("Encerrando o aplicativo. Até logo!")

def opcao_invalida():
    print("Opção inválida\n")
    input("Digite uma tecla para retornar ao menu: ")
    main ()
    

def main():
    os.system("cls")
    exibir_nome_programa()
    exibir_menu()
    processar_opcao()

if __name__ == "__main__":
   main()