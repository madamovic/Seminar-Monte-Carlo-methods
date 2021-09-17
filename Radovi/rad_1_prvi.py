# -*- coding: utf-8 -*-
import pyalps
import matplotlib.pyplot as plt
import pyalps.plot
import numpy as np

#prepare the input parameters
parms = []
for l in [4,6,8,10,12,14,16]:
	for t in np.linspace(0.1,3.0,30):
		parms.append(
        { 
        'LATTICE'        : "simple cubic lattice", 
        'MODEL'          : "spin",
        'local_S'        : 0.5,
        'T'              : t,
        'J'              : 1,
        'THERMALIZATION' : 50000,
        'SWEEPS'         : 100000,
        'L'              : l
        }
    )

#write the input file and run the simulation
input_file = pyalps.writeInputFiles('parmCa',parms)
pyalps.runApplication('dirloop_sse',input_file)

#load the susceptibility and collect it as function of temperature T
data = pyalps.loadMeasurements(pyalps.getResultFiles(prefix='parmCa'),'Stiffness')
stiffness =pyalps.collectXY(data,x='T',y='Stiffness', foreach=['L'])

for q in stiffness:
    q.y = q.y*q.props['L']

#make plot    
plt.figure()
pyalps.plot.plot(stiffness)
plt.xlabel(r'$T$')
plt.ylabel(r'$\rho_{s} L$')
plt.title(u'Hajzenbergov model na prostoj kubnoj rešetki')
plt.legend(loc='best')
plt.savefig("heisenberg_SC_1.eps",dpi=300)

plt.figure()
pyalps.plot.plot(stiffness)
plt.xlabel(r'$T$')
plt.ylabel(r'$\rho_{s} L$')
plt.xlim(0.98,1.1)
plt.ylim(0,3)
plt.title(u'Hajzenbergov model na prostoj kubnoj rešetki')
plt.legend(loc='best')
plt.savefig("heisenberg_SC_2.eps",dpi=300)

red=stiffness

for d in red:
    d.x=np.around(d.x,1)


lvrednost=np.array([q.props['L'] for q in red])
sel=np.argsort(lvrednost)
red=np.array(red)
red=red[sel]

s=open('redosled_rad_jedan.txt','w')
s.write(pyalps.plot.convertToText(red))
s.close()
