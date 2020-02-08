import api
a = api.conjunto('vogais')#É passado como parametro o nome do conjunto
#Função responsavel por inserir elementos no conjunto
a.push('a')
a.push('e')
a.push('i')
#aqui é inserido um elemento que ja existe no conjunto. OBS: elemento não sera repetido
a.push('a')
a.push('o')
a.push('u')
a.imprimir()
