import api

a = api.Conjunto('A')#É passado como parametro o nome do conjunto
#Função responsavel por inserir elementos no conjunto
a.inserir('a')
a.inserir('e')
a.inserir('i')
a.inserir('a')#aqui é inserido um elemento que ja existe no conjunto. OBS: elemento não sera repetido
a.inserir('o')
a.inserir('u')
#print('Tamanho',a.tamanho())
a.imprimir()
#print('Pertence:',a.pertence('c'))
B = api.Conjunto('B')
B.inserir('a')
B.inserir('e')
B.inserir('i')
B.inserir('u')
B.imprimir()
#print('subconjunto',a.eh_subconjunto(B))
#print('Contem propriamente:',a.contem_propriamente(B))
c = api.Conjunto('C')
c.inserir('a')
c.inserir('b')
c.inserir('c')
c.inserir('u')
c.imprimir()
'''
print('União:',a.uniao(B,c))
print('Diferença:',a.diferenca(B))

n1 = api.Conjunto('n1')
for i in range(0,10000,2):
    n1.inserir(i)
n2 =api.Conjunto('n2')
for i in range(10000,20000):
    n2.inserir(i)

print(n1.uniao(n2))
print(n1.uniao(n2))
print('Memoria:',api.memoria)
'''

print('Universo:',api.UNIVERSO)
print('complemento:', a.complemento())
print('complemento:', B.complemento())
print('conjunto das partes:',a.conjuntoDasPartes())
