from itertools import combinations
MEMORIA  = dict()
UNIVERSO = list()
class Conjunto():
    def __init__(self,nome):
        self.nome = nome
        self.elementos = list()
    def inserir(self,valor):
        if valor not in self.elementos:
            self.elementos.append(valor)
        if valor not in UNIVERSO:
            UNIVERSO.append(valor)
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
        nome = self.nome
        for n in args:
            nome += '_U_'+n.nome
        if nome in MEMORIA:
            return MEMORIA[nome]
        else:
            ret = Conjunto(nome)
            for i in self.elementos:
                ret.inserir(i)
            for a in args:
                for v in a.elementos:
                    if v not in self.elementos:
                        ret.inserir(v)
            MEMORIA[nome] = ret
            return ret
    def interseccao(self,*args):
        nome = self.nome
        for n in args:
            nome += '_\cap_'+n.nome
        ret= Conjunto(nome)
        todos_elementos=[]
        for i in args:
            for x in i.elementos:
                todos_elementos.append(x)

        for e in todos_elementos:            
            if e in self.elementos:
                if todos_elementos.count(e) == len(args): #se o elemento se repetir a mesma quantidade que o numero de conjuntos, quer dizer que ele está em todos eles
                    ret.inserir(e)

        return ret.elementos
    def diferenca(self,*args):
        nome = self.nome
        for n in args:
            nome += ' - '+n.nome
        ret = Conjunto(nome)
        get = []
        for i in args:
            for z in i.elementos:
                get.append(z)
        conj= self.elementos
        for element in conj:
            if element not in get:
                print(element)
                ret.inserir(element)
        return ret.elementos
    def complemento(self):
        ret = Conjunto('Complemento_de_'+self.nome)
        for i in UNIVERSO:
            if i not in self.elementos:
                ret.inserir(i)
        return ret.elementos

    def conjuntoDasPartes(self):
        arr = self.elementos
        result= []
        for i in range(1, len(arr)+1):
            result.extend(set(combinations(arr,i)))

        print(result)
        return result


        






        
