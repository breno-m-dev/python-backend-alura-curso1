class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title() #title() torna a primeira letra da string em maiuscula
        self.categoria = categoria
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self): #preciso colocar o self, para indicar que referencia a instancia atual da classe
        return f'{self._nome} | {self._categoria}'
        
    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    
    @classmethod
    def listar_restaurantes(cls):
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}')    
    
    def alternar_estado(self):
        self._ativo = not self._ativo


# Criando instâncias da classe Restaurante usando o construtor __init__
restaurante_praca = Restaurante('Praça', 'Churrascaria')
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('TOP PIZZA', 'Italiana')

Restaurante.listar_restaurantes()


def alternar_estado(self):
    """Alterna o estado de ativo do restaurante."""
    self._ativo = not self._ativo

# # A função vars() retorna os atributos de um objeto como um dicionário
# print('Restaurante 1:')
# #print(vars(restaurante_praca))
# print(restaurante_praca)

# print('\nRestaurante 2:')
# #print(vars(restaurante_pizza))
# print(restaurante_pizza)