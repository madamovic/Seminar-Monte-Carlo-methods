# -*- coding: utf-8 -*-
import pyalps
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pyalps.plot
#%matplotlib inline
import numpy as np

#prepare the input parameters4,6,8,12,14
tstart = 0.0
tstop = 4.0
steps = 41
parms = []
for l in [4,6,8,10]: 
    for t in np.linspace(tstart,tstop,steps):
        parms.append(
            { 
              'LATTICE'        : "square lattice",
              'T'              : t,
              'J'              : 1 ,
              'THERMALIZATION' : 100000,
              'SWEEPS'         : 1000000,
              'UPDATE'         : "cluster",
              'MODEL'          : "Ising",
              'L'              : l
            }
    )
#write the input file and run the simulation
input_file = pyalps.writeInputFiles('parm',parms)
pyalps.runApplication('spinmc',input_file,Tmin=5)
# use the following instead if you have MPI
#pyalps.runApplication('spinmc',input_file,Tmin=5,MPI=2)

pyalps.evaluateSpinMC(pyalps.getResultFiles(prefix='parm'))

#load the susceptibility and collect it as function of temperature T
data = pyalps.loadMeasurements(pyalps.getResultFiles(prefix='parm'),['|Magnetization|', 'Connected Susceptibility', 'Specific Heat', 'Binder Cumulant', 'Binder Cumulant U2'])
magnetization_abs = pyalps.collectXY(data,x='T',y='|Magnetization|',foreach=['L'])
connected_susc = pyalps.collectXY(data,x='T',y='Connected Susceptibility',foreach=['L'])
spec_heat = pyalps.collectXY(data,x='T',y='Specific Heat',foreach=['L'])
binder_u4 = pyalps.collectXY(data,x='T',y='Binder Cumulant',foreach=['L'])




f = open('podaci.txt','w')
f.write('# steps = '+str(steps)+' \n')
f.write(pyalps.plot.convertToText(magnetization_abs))
f.write(pyalps.plot.convertToText(connected_susc))
f.write(pyalps.plot.convertToText(spec_heat))
f.write(pyalps.plot.convertToText(binder_u4))
f.close()

