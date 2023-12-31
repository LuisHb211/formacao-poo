from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        #coloca-se esses atributos como privados, pois assim nao eh possivel que o usuario acesse-os diretamente
        self._nome = nome.title()
        self._categoria = categoria.upper()
        
        #Definindo o atributo 'ativo' como privado, por convencao, utilizando '_'
        self._ativo = False
        
        self._avaliacao = []
        
        #Acesso da Classe -> Variavel -> Funcao -> proprio objeto
        Restaurante.restaurantes.append(self)
        
    def __str__(self):
        return f'{self._nome} | {self._categoria}'
    
    #O uso do classmethod se da, pois esse metodo nao eh necessario de ser instanciado, ele eh da propria classe
    @classmethod
    def listar_restaurante(cls):
        #Cada objeto na lista (Restaurante.restaurantes) fara um print dos itens
        print(f"{'Nome do restaurante'.ljust(20)} | {'Categoria'.ljust(20)} | {'Avaliacao'.ljust(20)} | {'Status'}")
        for restaurante in cls.restaurantes:
            
            #Nao irei acessar o atributo _ativo nesse caso e sim o metodo que ira printar ativado ou desativado
            #Necessidade de usar str() se da, pois um objeto float nao tem o metodo ljust
            print(f"{restaurante._nome.ljust(20)} | {restaurante._categoria.ljust(20)} | {str(restaurante.media_avaliacoes).ljust(20)} | {restaurante.ativo} ") 
    
    #Usa-se a property para que um metodo seja acessado como atributo, sem a necessidade de chama-lo como uma funcao
    @property
    def ativo(self):
        return 'Ativado' if self._ativo else 'Desativado'   
    
    def alternar_status(self):
        self._ativo = not self._ativo
        
    def receber_avaliacao(self, cliente, nota):
        if 0 <=  nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
            return '-'
        soma_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_notas = len(self._avaliacao)
        media = round(soma_notas / quantidade_notas, 1)
        return media