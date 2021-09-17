# -*- coding: utf-8 -*-
import pyalps
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pyalps.plot
import numpy as np

#prepare the input parameters
parms = []
for r in [-0.4,-0.3,-0.2,-0.1,0.0,0.1,0.2,0.3,0.4]: 
    for t in np.linspace(0.1,5.0,51):
        parms.append(
            { 
              'LATTICE'        : "resetka_1",
              'LATTICE_LIBRARY' : "resetka_1.xml", 
              'T'              : t,
              'J0'              : 1 ,
              'J1'              : r*1,
              'THERMALIZATION' : 10000,
              'SWEEPS'         : 100000,
              'UPDATE'         : "cluster",
              'MODEL'          : "Heisenberg",
              'L'              : 16
            })
    
input_file = pyalps.writeInputFiles('parmRevB1a',parms)
pyalps.runApplication('spinmc',input_file,Tmin=5)
pyalps.evaluateSpinMC(pyalps.getResultFiles(prefix='parmRevB1a'))
data = pyalps.loadMeasurements(pyalps.getResultFiles(prefix='parmRevB1a'),['Specific Heat'])
spec_heat = pyalps.collectXY(data,x='T',y='Specific Heat',foreach=['J1'])


plt.figure()
pyalps.plot.plot(spec_heat)
plt.xlabel('Temperatura $T$')
plt.ylabel(u'Specifična toplota $C_{V}$')
plt.title(u'Klasični 2D Hajzenbergov model')
plt.legend(loc='best')
plt.savefig("heisenberg_Rev_B_klasicni_kap.eps",dpi=300)


