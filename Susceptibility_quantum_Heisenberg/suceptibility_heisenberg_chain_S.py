# -*- coding: utf-8 -*-
import pyalps
import matplotlib.pyplot as plt
import pyalps.plot
import numpy as np

#prepare the input parameters
parms = []
for s in [0.5,1.0,1.5,2.0]:
  for t in np.linspace(0.05,3.0,31):
    parms.append(
    { 
    'LATTICE'        : "chain lattice", 
    'MODEL'          : "spin",
    'local_S'        : s,
    'T'              : t,
    'J'              : 1 ,
    'THERMALIZATION' : 5000,
    'SWEEPS'         : 50000,
    'L'              : 20,
    'ALGORITHM'      : "loop"
    }
  )

#write the input file and run the simulation
input_file = pyalps.writeInputFiles('parmCS',parms)
pyalps.runApplication('loop',input_file)

#load the susceptibility and collect it as function of temperature T
data = pyalps.loadMeasurements(pyalps.getResultFiles(prefix='parmCS'),'Susceptibility')
susceptibility = pyalps.collectXY(data,x='T',y='Susceptibility', foreach=['local_S'])

#make plot
plt.figure()
pyalps.plot.plot(susceptibility)
plt.xlabel('Temperatura')
plt.ylabel('Susceptibilnost')
plt.legend(loc='best')
plt.title('Kvantni Hajzenbergov lanac (Quantum Heisenberg chain)')
plt.savefig("susc_heisenberg_chain_S.eps",dpi=300)
