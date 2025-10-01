import matplotlib.pyplot as plot
import numpy as np
ling_prog = np.array(["python","js","java","c"])
votos = np.array([100,30,5,15])
plot.pie(votos,labels=ling_prog)
# se por explodes=var(array) ele muda um pouco
#autopct troca o tipo de valor mostrado para porcentagem
#pctdistance move a pos de autopct
#startangle(troca onde começa o grafico)
plot.show()