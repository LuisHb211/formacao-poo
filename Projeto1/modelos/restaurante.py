from modelos.avaliacao import Avaliacao
from modelos.cardapio.item_cardapio import ItemCardapio
class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        #coloca-se esses atributos como privados, pois assim nao eh possivel que o usuario acesse-os diretamente
        self._nome = nome.title()
        self._categoria = categoria.upper()
        
        #Definindo o atributo 'ativo' como privado, por convencao, utilizando '_'
        self._ativo = False
        
        self._avaliacao = []
        
        self._cardapio = []
        
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
    
    '''
    Usa-se a property para que um metodo seja acessado como atributo, 
    sem a necessidade de chama-lo como uma funcao,
    quando necessita-se apenas executar a funcao, sem manipular/alterar
    '''
    
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
    
    
    '''
    As funcoes abaixos sao praticamente as mesmas, para nao repetir codigo no programa as funcoes 
    serao subsstituidos pela funcao abaixo (refatoracao)
    
    def adicionar_bebida_no_cardapio(self, bebida):
        self._cardapio.append(bebida)
        
    def adicionar_prato_no_cardapio(self, prato):
        self._cardapio.append(prato)
    '''
    
    #Essa funcao apenas confere se o item passado eh uma instancia da classe item_cardapio e se for adiciona na lista cardapio
    def adicionar_cardapio(self, item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)
            
    @property        
    def exibir_cardapio(self):
        print(f"Cardapio do restaurante {self._nome}\n")
        '''
        -> A funcao abaixa percorre a lista self._cardapio e comeca em 1
        -> A variavel i armazena o indice atual
        -> A variavel item armazena o objeto da lista percorrida
        -> Ao percorrer a lista e apontar para o primeiro objeto, sera acessado o seu item._nome e item._preco
        
        # for i,item in enumerate(self._cardapio, start=1):
        #     mensagem = f"{i}. Nome: {item._nome} | preco: RS{item._preco}"
        #     print(mensagem)
        '''
        
        '''
        Como no cardapio tem pratos e bebidas, faz sentido verificar se o objeto passado em item eh um prato ou bebida, assim basta usar a funcao hasattr() que verificar se o objeto tem o atributo x.
        Assim consegue-se diferenciar o print 
        '''
        for i,item in enumerate(self._cardapio, start=1):
            if hasattr(item, '_descricao'):
                mensagem_prato = f"{i}. Nome: {item._nome} | Preco: RS{item._preco} | Descricao: {item._descricao}"
                print(mensagem_prato)
            else:
                mensagem_bebida = f"{i}. Nome: {item._nome} | Preco: RS{item._preco} | Tamanho: {item._tamanho}"
                print(mensagem_bebida)