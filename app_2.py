from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
restaurante_japones = Restaurante('Japa', 'Japonesa')

restaurante_mexicano.alternar_estado()
restaurante_praca.alternar_estado()
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Lais', 8.5)
restaurante_praca.receber_avaliacao('Emy', 3)
restaurante_mexicano.receber_avaliacao('Emy', 0)
#
def main():
    Restaurante.listar_restaurantes()
    print(f'Media restaurante praca: {restaurante_praca.media_avaliacoes:.1f}')

if __name__ == '__main__':
    main()