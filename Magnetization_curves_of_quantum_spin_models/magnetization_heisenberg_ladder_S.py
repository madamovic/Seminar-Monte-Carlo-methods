# -*- coding: utf-8 -*-
import pyalps
import matplotlib.pyplot as plt
import pyalps.plot
import numpy as np

#prepare the input parameters
#parms = []
#for s in [0.5,1.0,1.5,2.0]:
#  for h in np.linspace(0.0,10.0,101):
#    parms.append(
#      { 
#      'LATTICE'        : "ladder", 
#      'MODEL'          : "spin",
#      'local_S'        : s,
#      'T'              : 0.08,
#     'J0'             : 1 ,
#     'J1'             : 1 ,
#      'THERMALIZATION' : 10000,
#      'SWEEPS'         : 100000,
#      'L'              : 20,
#      'h'              : h
#      }
#  )

#write the input file and run the simulation
#input_file = pyalps.writeInputFiles('parmHladS',parms)
#res = pyalps.runApplication('dirloop_sse',input_file,Tmin=5)

#load the magnetization and collect it as function of field h
data = pyalps.loadMeasurements(pyalps.getResultFiles(prefix='parmHladS'),'Magnetization Density')
magnetization = pyalps.collectXY(data,x='h',y='Magnetization Density', foreach=['local_S'])

#make plot
plt.figure()
pyalps.plot.plot(magnetization)
plt.xlabel('$h$')
plt.ylabel('Magnetizacija')
plt.ylim(0.0,2.1)
plt.title(u'Kvantni Hajzenbergov model, merdevinasti aranžman (Quantum Heisenberg ladder)',fontsize=8)
plt.legend(loc='best')
plt.savefig("magnetization_heisenberg_ladder_S.eps",dpi=300)
