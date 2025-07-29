class Restaurante:
    nome  = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Churrascaria'

restaurante_pizza = Restaurante()

print(vars(restaurante_praca))