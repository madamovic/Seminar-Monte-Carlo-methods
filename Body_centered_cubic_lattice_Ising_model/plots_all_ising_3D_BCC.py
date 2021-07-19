# -*- coding: utf-8 -*-
import pyalps
import time
start_time = time.time()
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pyalps.plot
#%matplotlib inline
import numpy as np

#prepare the input parameters4,6,8,12,14
parms = []
for l in [4,6,8,10,12]: 
    for t in np.linspace(0.0,9.0,91):
        parms.append(
            { 
              'LATTICE'        : "bcc",
              'LATTICE_LIBRARY' : "bcc.xml", 
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
input_file = pyalps.writeInputFiles('parmBCCa',parms)
pyalps.runApplication('spinmc',input_file,Tmin=5)
# use the following instead if you have MPI
#pyalps.runApplication('spinmc',input_file,Tmin=5,MPI=2)

pyalps.evaluateSpinMC(pyalps.getResultFiles(prefix='parmBCCa'))

#load the susceptibility and collect it as function of temperature T
data = pyalps.loadMeasurements(pyalps.getResultFiles(prefix='parmBCCa'),['|Magnetization|', 'Connected Susceptibility', 'Specific Heat', 'Binder Cumulant', 'Binder Cumulant U2'])
magnetization_abs = pyalps.collectXY(data,x='T',y='|Magnetization|',foreach=['L'])
connected_susc = pyalps.collectXY(data,x='T',y='Connected Susceptibility',foreach=['L'])
spec_heat = pyalps.collectXY(data,x='T',y='Specific Heat',foreach=['L'])
binder_u4 = pyalps.collectXY(data,x='T',y='Binder Cumulant',foreach=['L'])
binder_u2 = pyalps.collectXY(data,x='T',y='Binder Cumulant U2',foreach=['L'])

#make plots
plt.figure()
pyalps.plot.plot(magnetization_abs)
plt.xlabel('Temperatura $T$')
plt.ylabel('Magnetizacija $|m|$')
plt.title(u'3D Izingov model na zapreminski centriranoj kubnoj rešetki')
plt.legend(loc='best')
plt.savefig("figure_BCC_1.eps",dpi=300)

plt.figure()
pyalps.plot.plot(connected_susc)
plt.xlabel('Temperatura $T$')
plt.ylabel('Susceptibilnost $\chi$')
plt.title(u'3D Izingov model na zapreminski centriranoj kubnoj rešetki')
plt.legend(loc='best')
plt.savefig("figure_BCC_2.eps",dpi=300)

plt.figure()
pyalps.plot.plot(spec_heat)
plt.xlabel('Temperatura $T$')
plt.ylabel(u'Specifična toplota $C_{V}$')
plt.title(u'3D Izingov model na zapreminski centriranoj kubnoj rešetki')
plt.legend(loc='best')
plt.savefig("figure_BCC_3.eps",dpi=300)

plt.figure()
pyalps.plot.plot(binder_u4)
plt.xlabel('Temperatura $T$')
plt.ylabel('Binderov kumulant $U_{4}$')
plt.title(u'3D Izingov model na zapreminski centriranoj kubnoj rešetki')
plt.legend(loc='best')
plt.savefig("figure_BCC_4.eps",dpi=300)

plt.figure()
pyalps.plot.plot(binder_u2)
plt.xlabel('Temperatura $T$')
plt.ylabel('Binderov kumulant $U_{2}$')
plt.title(u'3D Izingov model na zapreminski centriranoj kubnoj rešetki')
plt.legend(loc='best')
plt.savefig("figure_BCC_5.eps",dpi=300)

f = open('binderdata_3D_Ising_BCC.txt','w')
f.write(pyalps.plot.convertToText(binder_u4))
f.close()

# ROUND
r=binder_u4

for d in r:
    d.x = np.around(d.x,1)

fg = open('binderdata_rounded_t_3D_Ising_BCC.txt','w')
fg.write(pyalps.plot.convertToText(r))
fg.close()

#REDOSLED

red=binder_u4

for d in red:
    d.x=np.around(d.x,1)

fh=open('binderdata_rounded_t_3D_Ising_BCC.txt','w')
fh.write(pyalps.plot.convertToText(red))
fh.close()

lvrednost=np.array([q.props['L'] for q in red])
sel=np.argsort(lvrednost)
red=np.array(red)
red=red[sel]

s=open('binderdata_rounded_t_redosled_3D_Ising_BCC.txt','w')
s.write(pyalps.plot.convertToText(red))
s.close()

print("--- %s seconds ---" % (time.time() - start_time))