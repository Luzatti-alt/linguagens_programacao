import matplotlib.pyplot as plot
import numpy as np
#versão optimizada com numpy
x = np.array(["web","sistemas","iot"])
y = np.array([10,5,50])
plot.bar(x,y,color="red")#c é parte de customização
plot.show()