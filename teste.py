import api
a = api.Conjunto('vogais')#É passado como parametro o nome do conjunto
#Função responsavel por inserir elementos no conjunto
a.push('a')
a.push('e')
a.push('i')
a.push('a')#aqui é inserido um elemento que ja existe no conjunto. OBS: elemento não sera repetido
a.push('o')
a.push('u')
print('Tamanho',a.tamanho())
a.imprimir()
print('Pertence:',a.pertence('c'))
B = api.Conjunto('B')
B.push('e')
B.push('i')
B.push('u')
print('subconjunto',a.eh_subconjunto(B))
print('Contem propriamente:',a.contem_propriamente(B))

'''
A = {a,b}
B = {b}

A é subconjunto de B? Não
A.eh_subconjunto(B)

A.contem(B)
B é subconjunto de A? Sim

'''