from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praca', 'Gourmet')
restaurante_praca.receber_avaliacao('Gui', 10)
restaurante_praca.receber_avaliacao('Luis', 8)
restaurante_praca.receber_avaliacao('Fred', 5)

restaurante_chines = Restaurante('Restaurante', 'Chinesa')
restaurante_chines.alternar_status()

def main():
    Restaurante.listar_restaurante()






if __name__ == '__main__':
    main()