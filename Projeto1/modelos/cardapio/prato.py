from modelos.cardapio.item_cardapio import ItemCardapio

'''
-> A classe prato eh uma filha da classe item_cardapio, assim basta importa-la
    e passar o nome da classe mae na frente da classe filha, entre parenteses.
    
-> Para que a classe filha herde atributos da mae eh necessario utilizar a funcao super()
    e logo apos o metodo e seus atributos
    
-> Assim concretiza-se a chamada heranca
'''
class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao
        
    def __str__(self)   :
        return self._nome
    
    '''
    A aplicação dessa funcao eh necessaria devido a classe mae ter ela como abstractmethod, assim eh necessario cria-la nas filhas. Isso eh chamado poliomorfismo, a modelacao de funcoes em diferentes classes, ou seja uma adaptacao.
    '''
    def aplicar_desconto(self):
        self._preco -= (self._preco*0.05)