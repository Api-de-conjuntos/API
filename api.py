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
                
                if v not in self.elementos:
                    u.push(v)

        uni=u.elementos
        return uni

    def interseccao(self,*args):
        i= Conjunto('Intersecção')
        get=[]
        for a in args:
            valor= a.elementos
            get.append(valor)   #vou pegar todos os conjuntos que estão em args e colocar em uma lista
        
        string=''
        for x in range(len(get)):   #tentem melhorar essa parte, eu só consegui dessa forma juntar todos os elementos
            for j in get[x]:
                string=string+j+' '
        
        s=string.split()
        
        for e in s:
            
            if e in self.elementos:
                if str(s.count(e)) == str(len(get)):  #se o elemento se repetir a mesma quantidade que o numero de conjuntos, quer dizer que ele está em todos eles
                    i.push(e)

        inter= i.elementos
        return inter
                    
                
        






        
