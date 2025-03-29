# Definição da classe Pessoa 
class Pessoa:
    # Método Construtor 
    # é chamado quando criamos um objeto
    def __init__(self, nome, idade, altura):
        # Atribuir valores aos atributos
        self.nome = nome    
        self.idade = idade  
        self.altura = altura   
    
    def apresentar(self):   
        print(f'Olá, meu nome é {self.nome} e tenho {self.idade} anos.')
        print(f'Eu tenho {self.altura} de altura.')    
        

# Criando objetos da classe Pessoa
p1 = Pessoa("Rafael", 34, "1.50")
p2 = Pessoa("Guilherme", 7, "1.35")
p3 = Pessoa("Alberto", 18, "1.95")

# Chamando o método para apresentar os dados dos objetos
p1.apresentar()
p2.apresentar()
p3.apresentar()
