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
print('subconjunto',a.eh_subconjunto(['b','d','c']))
print('Contem propriamente:',a.contem_propriamente(['a','e','i','o']))