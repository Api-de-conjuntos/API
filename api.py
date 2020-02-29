class Conjunto():
    def __init__(self,nome):
        self.nome = nome
        self.elementos = list()
    def push(self,valor):
        if valor not in self.elementos:
            self.elementos.append(valor)
    def tamanho(self):
        return len(self.elementos)
    def imprimir(self):
        print('Nome do conjunto: {}\nElementos:{}'.format(self.nome,self.elementos))
    def pertence(self, valor):
        if valor in self.elementos:
            return True
        else:
            return False
    def eh_subconjunto(self, valor):
        for i in valor.elementos:
            if i in self.elementos:
                return True
        return False
    def contem_propriamente(self, valor):
        retorno = []
        if len(valor.elementos) == len(self.elementos):
            return False
        else:
            for i in valor.elementos:
                if i in self.elementos:
                    pass
                else:
                    return False
            return True

    def uniao(self,B,c):
        u= Conjunto('União')
        for i in self.elementos:
            if i not in B.elementos:
                u.push(i)
        for i in B.elementos:
            u.push(i)
        for i in c.elementos:
            if i not in u.elementos:
                u.push(i)
        print(u.elementos)

    def interseccao(self,c):
        i= Conjunto('Intersecção')
        for j in self.elementos:
            if j in c.elementos:
                i.push(j)

        print("Intersecção:",i.elementos)