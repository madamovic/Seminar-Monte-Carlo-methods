# -*- coding: utf-8 -*-
import pyalps
import matplotlib.pyplot as plt
import pyalps.plot
import numpy as np

#prepare the input parameters
parms = []
for t in np.linspace(0.05,3.0,31):
    parms.append(
        { 
          'LATTICE'        : "chain lattice", 
          'MODEL'          : "spin",
          'local_S'        : 0.5,
          'T'              : t,
          'J'              : 1 ,
          'THERMALIZATION' : 5000,
          'SWEEPS'         : 50000,
          'L'              : 60,
          'ALGORITHM'      : "loop"
        }
    )

#write the input file and run the simulation
input_file = pyalps.writeInputFiles('parmC',parms)
pyalps.runApplication('loop',input_file)

#load the susceptibility and collect it as function of temperature T
data = pyalps.loadMeasurements(pyalps.getResultFiles(prefix='parmC'),'Susceptibility')
susceptibility = pyalps.collectXY(data,x='T',y='Susceptibility')

#make plot
plt.figure()
pyalps.plot.plot(susceptibility)
plt.xlabel('Temperatura')
plt.ylabel('Susceptibilnost')
plt.title('Kvantni Hajzenbergov lanac (Quantum Heisenberg chain)')
plt.savefig("susc_heisenberg_chain.eps",dpi=300)
