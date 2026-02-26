import os

def exibir_nome_programa():
    print("Sabor Express\n")

def exibir_menu():

    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Ativar restaurante")
    print("4. Sair\n")

    opcao_escolhida = int(input("Escolha uma opção: "))
    print(f"Opção escolhida: {opcao_escolhida}")

def processar_opcao(opcao_escolhida):

    if opcao_escolhida == 1:
        print("Cadastrar restaurante selecionado.")
    elif opcao_escolhida == 2:
        print("Listar restaurante selecionado.")
    elif opcao_escolhida == 3:
        print("Ativar restaurante selecionado.")
    else:
        finalizar_app()

def finalizar_app():
    os.system ("cls")
    print("Encerrando o aplicativo. Até logo!") 

def main():
    exibir_nome_programa()
    exibir_menu()
    opcao_escolhida = int(input("Escolha uma opção: "))
    processar_opcao(opcao_escolhida)
if __name__ == "__main__":   
    main()