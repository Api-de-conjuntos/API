class conjunto():
    def __init__(self,nome):
        self.nome = nome
        self.elementos = list()
    def push(self,valor):
        if valor not in self.elementos:
            self.elementos.append(valor)
    def tamanho(self):
        return len(self.elementos)
    def imprimir(self):
        print('Nome do conjunto:{}\nElementos:{}'.format(self.nome,self.elementos))

