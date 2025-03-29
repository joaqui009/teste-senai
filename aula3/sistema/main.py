from app.controllers.clienteController import clienteController 

def exibir_menu():
    print("\n====MENU====")
    print("1 - Cadadstrar Cliente")
    print("2 - Listar Clientes")
    print("3 - Cadastrar Produto")
    print("4 - Listar Produtos")
    print("0 - Sair do Sistema")
    
def main():
    cntrlCliente = clienteController()
    
    while True: 
        exibir_menu()
        opc = input("Escolha uma opição: ")
        
        if opc == "1":
            nome = input("Nome Do Cliente:")
            email = input("E-mail: ")
            idade = int(input("Idade: "))
            # Salvariamos no banco de dados 
            cntrlCliente.criar_cliente(nome, email, idade)
            
        elif opc == "2":
            # Listar do banco de dados os clientes 
            clientes = cntrlCliente.listar_clientes()
            for index, cliente in enumerate(clientes, 1):
                # index -> Posição atual do cliente listado
                # __str__ -> cliente => Cliente(nome="", email="", idade="")
                print(F"{index}. {cliente}")
            
        elif opc == "3":
            nome = input("nome do produto")
            peco = float(input("Preço: "))
        elif opc == "4":
            # listar do banco de dados os produtos
            print("listar")
        elif opc == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção Inválida. Tente novamente.")
            
if __name__ == "__main__":
    main()

# python main.py