import matplotlib.pyplot as plot
import numpy as np
x = np.random.random(50)*100#array do numpy
y = np.random.random(50)*100 #dados aleatorios para melhor demonstração
plot.scatter(x,y,marker="X")
#independente do tipo de grafico tem que ser do mesmo tamanho
#dentro de ()
plot.show()