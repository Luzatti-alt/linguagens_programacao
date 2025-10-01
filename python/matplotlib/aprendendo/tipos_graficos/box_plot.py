import matplotlib.pyplot as plot
import numpy as np
#versão optimizada com numpy
altura = np.random.normal(169,8,200)
plot.boxplot(altura)
#ss isso é um grafico
plot.show()