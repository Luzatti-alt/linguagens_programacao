import matplotlib.pyplot as plot
import numpy as np
#versão optimizada com numpy
x = np.random.random(5)
y = np.random.random(5)
plot.plot(x,y,c="green",lw=4,linestyle="--")#c é parte de customização
plot.show()