# -*- coding: utf-8 -*-
import pyalps
import matplotlib.pyplot as plt
import pyalps.plot
import numpy as np


#load the susceptibility and collect it as function of temperature T
data = pyalps.loadMeasurements(pyalps.getResultFiles(prefix='parmCa'),'Susceptibility')
susc =pyalps.collectXY(data,x='T',y='Susceptibility', foreach=['L'])


#make plot    
plt.figure()
pyalps.plot.plot(susc)
plt.xlabel(r'$T$')
plt.ylabel(r'$\chi$')
plt.title(u'Hajzenbergov model na prostoj kubnoj rešetki')
plt.legend(loc='best')
plt.savefig("heisenberg_SC_3.eps",dpi=300)


