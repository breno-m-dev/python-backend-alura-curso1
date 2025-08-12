from modelos.avaliacao import Avaliacao 
class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title() #title() torna a primeira letra da string em maiuscula
        self._categoria = categoria
        self._ativo = False
        self._avaliacoes = []
        Restaurante.restaurantes.append(self)

    def __str__(self): #preciso colocar o self, para indicar que referencia a instancia atual da classe
        return f'{self._nome} | {self._categoria}'
        
    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'
    
    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Estado'.ljust(25)} | {'media_avaliacoes'.ljust(25)}') 
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)}')    
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if not 0 <= nota <= 5:
            print('Valor de nota invalido, digite um numero entre 0 e 5')
        else:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacoes.append(avaliacao)

    @property
    def media_avaliacoes(self): #media das avaliacoes de um restaurante
        if (len(self._avaliacoes) == 0):
            return 'Nenhuma avaliação feita' 
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacoes)
        media =  round(soma_das_notas/len(self._avaliacoes) , 1)#round arredonda para ter 1 casa decimal
        if media:
            return media
        else:
            return 0
        
# # Criando instâncias da classe Restaurante usando o construtor __init__
# restaurante_praca = Restaurante('Praça', 'Churrascaria')
# restaurante_praca.alternar_estado()
# restaurante_pizza = Restaurante('TOP PIZZA', 'Italiana')

# Restaurante.listar_restaurantes()



# # # A função vars() retorna os atributos de um objeto como um dicionário
# # print('Restaurante 1:')
# # #print(vars(restaurante_praca))
# # print(restaurante_praca)

# # print('\nRestaurante 2:')
# # #print(vars(restaurante_pizza))
# # print(restaurante_pizza)