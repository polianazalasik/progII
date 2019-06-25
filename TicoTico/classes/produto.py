class Produto():
    def __init__(self, nom_produto, preco):
        self.nom_produto = nom_produto
        self.preco = preco

class Item():
    def __init__(self, produto, qtd):
        self.produto = produto
        self.qtd = qtd

class Carrinho():
    def __init__(self, data, hora, *produtos):
        self.data = data
        self.hora = hora
        self.produtos = list(produtos)

if __name__=="__main__":
    star = Produto("5Star", 3.50)
    coca_Cola = Produto("Coca-Cola", 9.00)
    banana = Produto("Banana", 1.99)
    barrinha = Produto("Barrinha de Cereal" , 1.15)
    
    item1 = Item(star, 3)
    item2 = Item(banana, 9)
    item3 = Item(barrinha, 30)

    print(star.produto, star.qtd)
