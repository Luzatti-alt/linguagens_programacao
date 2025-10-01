import matplotlib.pyplot as plot
import numpy as np
idades = np.random.normal(20,1.5,1000)
plot.hist(idades,
          bins=[idades.min(), 18,21,idades.max()])
#se for cumulativa tem que deixar como true dentro de plot.hist
#ou bins=20(coleções de bins)
#bins é tipo um limitador
plot.show()