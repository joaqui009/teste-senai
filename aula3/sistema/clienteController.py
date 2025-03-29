from ..models.cliente import Cliente
from ..database.database import BancoFake

class clienteController:
    def __init__(self):
        # conexao com o banco
        self.db = BancoFake()
        
    def criar_cliente(self, nome, email, idade):
        # criar o objeto cliente e salva no banco
        novo_cliente = Cliente(nome, email, idade)
        # converter para dict (json)
        dict_cliente = {
            "nome": novo_cliente.nome,
            "email": novo_cliente.email,
            "idade": novo_cliente.idade
        }
        # salvar no banco 
        self.db.adicionar_cliente(dict_cliente)
        print("Cliente cadastrado com sucesso!")
        
    def listar_clientes(self):
        """
        Retornar uma lista com todos os clientes
        """
        return self.db.listar_clientes()