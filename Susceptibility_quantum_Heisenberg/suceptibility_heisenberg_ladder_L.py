# -*- coding: utf-8 -*-
import pyalps
import matplotlib.pyplot as plt
import pyalps.plot
import numpy as np

#prepare the input parameters
parms = []
for l in [20,40,60,80,100]:
  for t in np.linspace(0.05,3.0,31):
    parms.append(
    { 
    'LATTICE'        : "ladder", 
    'MODEL'          : "spin",
    'local_S'        : 0.5,
    'T'              : t,
    'J0'             : 1,
    'J1'             : 1,
    'THERMALIZATION' : 5000,
    'SWEEPS'         : 50000,
    'L'              : l,
    'ALGORITHM'      : "loop"
    }
  )

#write the input file and run the simulation
input_file = pyalps.writeInputFiles('parmLL',parms)
pyalps.runApplication('loop',input_file)

#load the susceptibility and collect it as function of temperature T
data = pyalps.loadMeasurements(pyalps.getResultFiles(prefix='parmLL'),'Susceptibility')
susceptibility = pyalps.collectXY(data,x='T',y='Susceptibility', foreach=['L'])

#make plot
plt.figure()
pyalps.plot.plot(susceptibility)
plt.xlabel('Temperatura')
plt.ylabel('Susceptibilnost')
plt.legend(loc='best')
plt.title(u'Kvantni Hajzenbergov model, merdevinasti aranžman (Quantum Heisenberg ladder)',fontsize=8)
plt.savefig("susc_heisenberg_ladder_L.eps",dpi=300)
