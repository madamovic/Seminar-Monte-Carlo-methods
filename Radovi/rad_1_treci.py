# -*- coding: utf-8 -*-
import pyalps
import matplotlib.pyplot as plt
import pyalps.plot
import numpy as np


parms = []
for t in [0.99,1.0,1.01,1.02,1.03,1.04,1.05,1.06]:
	for l in [4,6,8,10,12,14,16]:
		parms.append(
        { 
        'LATTICE'        : "simple cubic lattice", 
        'MODEL'          : "spin",
        'local_S'        : 0.5,
        'T'              : t,
        'J'              : 1,
        'THERMALIZATION' : 10000,
        'SWEEPS'         : 100000,
        'L'              : l
        })
input_file = pyalps.writeInputFiles('parmCb',parms)
pyalps.runApplication('dirloop_sse',input_file)
data = pyalps.loadMeasurements(pyalps.getResultFiles(prefix='parmCb'),'Susceptibility')
susc =pyalps.collectXY(data,x='L',y='Susceptibility',foreach=['T'])


red=susc


lvrednost=np.array([q.props['T'] for q in red])
sel=np.argsort(lvrednost)
red=np.array(red)
red=red[sel]

s=open('redosled_rad_jedan_log.txt','w')
s.write(pyalps.plot.convertToText(red))
s.close()


file=open('redosled_rad_jedan_log.txt')

file_data=np.loadtxt(file,usecols=(0,1))

x=file_data[:,0]
y=file_data[:,1]

y = y/x**2
y = np.log(y)

x = np.log(x)

plt.figure()
plt.scatter(x[0:7],y[0:7],label='T=0.99')
plt.scatter(x[7:14],y[7:14],label='T=1.00')
plt.scatter(x[14:21],y[14:21],label='T=1.01')
plt.scatter(x[21:28],y[21:28],label='T=1.02')
plt.scatter(x[28:35],y[28:35],label='T=1.03')
plt.scatter(x[35:42],y[35:42],label='T=1.04')
plt.scatter(x[42:49],y[42:49],label='T=1.05')
plt.scatter(x[49:56],y[49:56],label='T=1.06')
plt.xlabel(r'$ln(L)$')
plt.ylabel(r'$ln(\chi/L^{2})$')
plt.legend(loc='best')
plt.savefig("heisenberg_SC_log.eps",dpi=300)




