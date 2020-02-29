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

    def uniao(self,*args):
        u= Conjunto('União')
        for i in self.elementos:
            u.push(i)
        for a in args:
            valor= a.elementos
            for v in valor:
                print(v)
                if v not in self.elementos:
                    u.push(v)
        print(u.elementos)

    def interseccao(self,*args):
        i= Conjunto('Intersecção')
        for a in args:
            valor= a.elementos
            print(valor)
            for v in valor:
                if v in self.elementos:
                    i.push(v)
        print("Intersecção:",i.elementos)