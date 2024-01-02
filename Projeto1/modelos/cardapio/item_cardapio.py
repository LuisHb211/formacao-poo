from abc import abstractmethod, ABC

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco
        
    '''
    Abstractmethod tem o intuito de propagar para todas as classes filhas a funcao abaixo. Sendo necessario a implementacao dessa funcao nas classes filhas, caso contrario ira falhar.
    '''
    @abstractmethod
    def aplicar_desconto(self):
        pass
    
    