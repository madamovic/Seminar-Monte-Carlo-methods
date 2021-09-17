# -*- coding: utf-8 -*-
import pyalps
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pyalps.plot
import numpy as np

#prepare the input parameters
parms = []
for c in [0.1,0.05,0.02,0.00]: 
    for t in np.linspace(0.01,5.0,51):
        parms.append(
            { 
              'LATTICE'        : "resetka_2",
              'LATTICE_LIBRARY' : "resetka_2.xml", 
              'T'              : t,
              'J0'              : 1 ,
              'J1'              : 0.1*1,
              'J2'              : c*1,
              'THERMALIZATION' : 100000,
              'SWEEPS'         : 1000000,
              'UPDATE'         : "cluster",
              'MODEL'          : "Heisenberg",
              'L'              : 20,
              'W'              : 20,
              'H'              : 10
            })
    
input_file = pyalps.writeInputFiles('parmRevB1b',parms)
pyalps.runApplication('spinmc',input_file,Tmin=5)
pyalps.evaluateSpinMC(pyalps.getResultFiles(prefix='parmRevB1b'))
data = pyalps.loadMeasurements(pyalps.getResultFiles(prefix='parmRevB1b'),['Specific Heat'])
spec_heat = pyalps.collectXY(data,x='T',y='Specific Heat',foreach=['J2'])

plt.figure()
pyalps.plot.plot(spec_heat)
plt.xlabel('Temperatura $T$')
plt.ylabel(u'Specifična toplota $C_{V}$')
plt.title(u'Klasični 3D Hajzenbergov model')
plt.legend(loc='best')
plt.savefig("heisenberg_Rev_B_klasicni_kap_c.eps",dpi=300)


