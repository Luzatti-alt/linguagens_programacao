import numpy as np
array = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]])#literalmente é um matrix
#array[inicio:fim:passo]
#slice é representado com :
#neste caso até que começa com 0 porem 
#o end(onde queremos chegar nn sera o mesmo número da camada do array)
#slicing[X:Y:Z] onde Z é uma regra ex se fosse 2 passaria o index 0,2,4,6,... 
print(array[0:3])#esse [index 0 -> index 2(nesse caso nn funciona com a logica de array)]
#se for [X:] ira ate o array acabar
#se for [::Z] funcionaria se for so o z nn pq z estaria na pos de x que é o inicio
#se quisermos um splicing de colunas [_:,_] se for : é linhas se for :, é coluna