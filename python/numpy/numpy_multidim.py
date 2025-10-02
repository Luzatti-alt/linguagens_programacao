import numpy as np
#array = np.array(['A','B',C])#uni dimensional
array = np.array([
    ['A','B','C'],
    ['D','E','F']
])#array de duas dimensoes
array_dois = np.array([
    [['A','B','C'],
     ['D','E','F'],
     ['G','H','I']
    ],#deste jeito ele fica organizado e mais legivel
    [['J','K','L'],
     ['M','N','O'],
     ['P','Q','R']
    ],
    [['S','T','U'],
     ['V','W','X'],
     ['Y','Z','_']
    ]
]#esse arrays tem que ter o mesmo tamanho/msm qnt de itens
                 )#array de três dimensoes
print('array 1:\n',array,'\n')
print(array.ndim," esse é o numero de dimensoes deste array(array)",'\n')
print('array 2:\n',array_dois,'\n')
print(array_dois.ndim," esse é o numero de dimensoes deste array(array_dois)",'\n')
#shape retorna como tupla(X,Y,Z)linhas,elementos,colunas
#acessando um valor especifico ex:
print(array_dois[0,0,0],'\n')#dentro de quantos tem em .shape(0-N)do array
#exemplo simple que pode ser pratico
palavra = array_dois[1,1,2] + array_dois[0,2,2]#indexing de multidimensionalidade
print(palavra)