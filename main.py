# Define a classe Produto para armazenar informações de um produto
class Produto:
    def __init__(self, Codigo, Nome, Preco):
        self.Codigo = Codigo
        self.Nome = Nome
        self.Preco = Preco
        
    def __str__(self):
        return '%d, %s, %f' % (self.Codigo, self.Nome, self.Preco)

# Define a classe Hash para implementar a tabela hash com endereçamento aberto
class Hash:
    def __init__(self, tamanho):
        self.__qtd = 0
        self.__TABLE_SIZE = tamanho
        self.__itens = [None for i in range(tamanho)]

    def __chaveDivisao(self, chave):
        # Função de hash usando o método da divisão
        return chave % self.__TABLE_SIZE

    def __sondagemLinear(self, pos, i):
        # Calcula a próxima posição usando sondagem linear
        return (pos + i) % self.__TABLE_SIZE
    
    def insereHash_EnderAberto(self, Codigo, Nome, Preco):
        # Verifica se a tabela está cheia
        if self.__qtd == self.__TABLE_SIZE:
            return False

        # Calcula a posição inicial usando a função de hash
        chave = Codigo
        pos = self.__chaveDivisao(chave)
        
        # Tenta inserir o item usando sondagem linear
        for i in range(self.__TABLE_SIZE):
            newPos = self.__sondagemLinear(pos, i)
            if self.__itens[newPos] is None:
                # Insere o produto na posição disponível
                self.__itens[newPos] = Produto(Codigo, Nome, Preco)
                self.__qtd += 1
                return True
            
        # Retorna False se não conseguir inserir (tabela cheia)
        return False

    def buscaHash_EnderAberto(self, Codigo):
        # Calcula a posição inicial usando a função de hash
        pos = self.__chaveDivisao(Codigo)
        
        for i in range(self.__TABLE_SIZE):
            newPos = self.__sondagemLinear(pos, i)
            if self.__itens[newPos] is None:
                # Retorna None se não encontrar o produto
                return None

            produto = self.__itens[newPos]
            if produto.Codigo == Codigo:
                # Retorna o produto se o código corresponder
                return produto

        # Retorna None se não encontrar o produto após verificar todas as posições
        return None

    def print(self):
      
        # Imprime a quantidade de itens e o tamanho da tabela
        print("Status da tabela: " + f'{self.__qtd} / {self.__TABLE_SIZE}')
        print("")
        
        # Imprime cada posição da tabela e o produto armazenado (se houver)
        for i in range(self.__TABLE_SIZE):
            print(f'{i}) {self.__itens[i]}')
        print("")

# ===================================================
# Exemplos de uso da classe Hash

# Cria uma tabela hash com tamanho 10
ha = Hash(10)

# Insere alguns produtos na tabela usando endereçamento aberto
ha.insereHash_EnderAberto(101, "Camiseta Grêmio Tam P", 129.99)
ha.insereHash_EnderAberto(102, "Livro: Estrutura de Dados e seus Algorítimos", 140.99)
ha.insereHash_EnderAberto(103, "Blusão Nike Feminino, Tam M", 39.99)
ha.insereHash_EnderAberto(104, "Lâmpada LED 12w", 49.99)

# ha.insereHash_EnderAberto(111, "Calção Grêmio Tam M", 49.99)

# Imprime o estado atual da tabela
ha.print()

# Busca um produto pelo código
x = ha.buscaHash_EnderAberto(103)

# Imprime os resultados da busca
print('Busca')
print(x)
