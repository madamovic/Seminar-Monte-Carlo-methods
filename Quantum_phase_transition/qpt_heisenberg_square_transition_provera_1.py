# -*- coding: utf-8 -*-
import pyalps
import matplotlib.pyplot as plt
import pyalps.plot
import numpy as np

parms = []
for l in [8,10,12,16]:
    for j2 in np.linspace(0.1,0.6,101):
        parms.append(
            { 
              'LATTICE'        : "coupled ladders", 
              'local_S'        : 0.5,
              'ALGORITHM'      : 'loop',
              'SEED'           : 0,
              'BETA'           : 4*l,
              'J0'             : 1 ,
              'J1'             : 1,
              'J2'             : j2,
              'THERMALIZATION' : 5000,
              'SWEEPS'         : 50000, 
              'MODEL'          : "spin",
              'L'              : l,
              'W'              : l
            }
    )
    
#write the input file and run the simulation
input_file = pyalps.writeInputFiles('parmpr1',parms)
pyalps.runApplication('loop',input_file)

data = pyalps.loadMeasurements(pyalps.getResultFiles(prefix='parmpr1'),['Binder Ratio of Staggered Magnetization','Stiffness'])

binder=pyalps.collectXY(data,x='J2',y='Binder Ratio of Staggered Magnetization', foreach=['L'])
stiffness =pyalps.collectXY(data,x='J2',y='Stiffness', foreach=['L'])

for q in stiffness:
    q.y = q.y*q.props['L']

#make plot    
plt.figure()
pyalps.plot.plot(stiffness)
plt.xlabel(r'$J_{2}$')
plt.ylabel(r'$\rho_{s} L$')
plt.title(u'Hajzenbergov model, 2D rešetka, merdevinasti aranžman (coupled ladders)')
plt.legend(loc='best')
plt.savefig("stiffness_transition_provera_1.eps",dpi=300)


plt.figure()
pyalps.plot.plot(binder)
plt.xlabel(r'$J_{2}$')
plt.ylabel(r'$U_{4}$')
plt.title(u'Hajzenbergov model, 2D rešetka, merdevinasti aranžman (coupled ladders)')
plt.legend(loc='best')
plt.savefig("binder_transition_provera_1.eps",dpi=300)

