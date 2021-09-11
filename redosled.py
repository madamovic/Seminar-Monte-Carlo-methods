import pyalps
import matplotlib.pyplot as plt
import pyalps.plot
import numpy as np


parms = []
for l in [4,8,16,24,48]: 
    for t in np.linspace(0.01,5.0,50):
        parms.append(
            { 
              'LATTICE'        : "square lattice", 
              'T'              : t,
              'J'              : 1 ,
              'THERMALIZATION' : 10000,
              'SWEEPS'         : 100000,
              'UPDATE'         : "cluster",
              'MODEL'          : "Ising",
              'L'              : l
            }
    )

input_file = pyalps.writeInputFiles('parm7a',parms)
pyalps.runApplication('spinmc',input_file,Tmin=5)


pyalps.evaluateSpinMC(pyalps.getResultFiles(prefix='parm7a'))

data = pyalps.loadMeasurements(pyalps.getResultFiles(prefix='parm7a'),['Binder Cumulant'])
binder_u4 = pyalps.collectXY(data,x='T',y='Binder Cumulant',foreach=['L'])

red=binder_u4

for d in red:
    d.x=np.around(d.x,1)

lvrednost=np.array([q.props['L'] for q in red])
sel=np.argsort(lvrednost)
red=np.array(red)
red=red[sel]

s=open('binderdata_redosled.txt','w')
s.write(pyalps.plot.convertToText(red))
s.close()

