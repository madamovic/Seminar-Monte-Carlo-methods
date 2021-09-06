# -*- coding: utf-8 -*-
import pyalps
import matplotlib.pyplot as plt
import pyalps.plot
import numpy as np

#prepare the input parameters
parms = []
for h in np.linspace(0.0,5.0,51):
    parms.append(
        { 
          'LATTICE'        : "ladder", 
          'MODEL'          : "spin",
          'local_S'        : 0.5,
          'T'              : 0.08,
          'J0'             : 1 ,
          'J1'             : 1 ,
          'THERMALIZATION' : 1000,
          'SWEEPS'         : 10000,
         'L'              : 20,
          'h'              : h
        }
    )

#write the input file and run the simulation
input_file = pyalps.writeInputFiles('parmHlad',parms)
res = pyalps.runApplication('dirloop_sse',input_file,Tmin=5)

#load the magnetization and collect it as function of field h
data = pyalps.loadMeasurements(pyalps.getResultFiles(prefix='parmHlad'),'Magnetization Density')
magnetization = pyalps.collectXY(data,x='h',y='Magnetization Density')

#make plot
plt.figure()
pyalps.plot.plot(magnetization)
plt.xlabel('$h$')
plt.ylabel('Magnetizacija')
plt.ylim(0.0,0.6)
plt.title(u'Hajzenbergov model, merdevinasti aranžman (Quantum Heisenberg ladder)',fontsize=8)
plt.savefig("magnetization_heisenberg_ladder.eps",dpi=300)