# -*- coding: utf-8 -*-
import pyalps
import matplotlib.pyplot as plt
import pyalps.plot
import numpy as np

#prepare the input parameters
tc=1.03
parms = []
for l in [4,6,8,10,12,14,16]:
	for t in np.linspace(tc+0.0,tc+3.0,31):
		parms.append(
        { 
        'LATTICE'        : "simple cubic lattice", 
        'MODEL'          : "spin",
        'local_S'        : 0.5,
        'T'              : t,
        'J'              : 1,
        'THERMALIZATION' : 500000,
        'SWEEPS'         : 500000,
        'L'              : l
        }
    )

#write the input file and run the simulation
input_file = pyalps.writeInputFiles('parmCc',parms)
pyalps.runApplication('dirloop_sse',input_file)

#load the susceptibility and collect it as function of temperature T
data = pyalps.loadMeasurements(pyalps.getResultFiles(prefix='parmCc'),'Susceptibility')
susc =pyalps.collectXY(data,x='T',y='Susceptibility', foreach=['L'])

for q in susc:
    q.y = q.y*(q.x-tc)**(1.3987)
    q.x=q.x-tc
    q.x=q.x**(0.71)
    q.x=q.x*q.props['L']

#make plot    
plt.figure()
pyalps.plot.plot(susc)
plt.xlabel(r'$L(T-T_{C})^{\nu}$')
plt.ylabel(r'$\chi(T-T_{C})^{\gamma}$')
plt.title(u'Hajzenbergov model na prostoj kubnoj rešetki')
plt.legend(loc='best')
plt.savefig("heisenberg_SC_5.eps",dpi=300)


