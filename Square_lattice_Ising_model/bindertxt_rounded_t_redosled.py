
# coding: utf-8

# In[61]:

import pyalps
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pyalps.plot
import numpy as np
import pyalps.fit_wrapper as fw

#prepare the input parameters
parms = []
for l in [10,20,30,40,50,60,70,80]:
    for t in np.linspace(0.0,4.0,40):
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

#write the input file and run the simulation
input_file = pyalps.writeInputFiles('parm7j',parms)
pyalps.runApplication('spinmc',input_file,Tmin=5)
# use the following instead if you have MPI
#pyalps.runApplication('spinmc',input_file,Tmin=5,MPI=4)

pyalps.evaluateSpinMC(pyalps.getResultFiles(prefix='parm7j'))

#load the susceptibility and collect it as function of temperature T
data = pyalps.loadMeasurements(pyalps.getResultFiles(prefix='parm7j'),'Binder Cumulant')

binder_u4 = pyalps.collectXY(data,x='T',y='Binder Cumulant',foreach=['L'])


binder_u4proba = pyalps.collectXY(data,x='T',y='Binder Cumulant',foreach=['L'])



for d in binder_u4:
    d.x=np.around(d.x,1)


f=open('binderdata_rounded_t.txt','w')
f.write(pyalps.plot.convertToText(binder_u4))
f.close()


# In[65]:

lvrednost=np.array([q.props['L'] for q in binder_u4])
print(lvrednost)


sel=np.argsort(lvrednost)
print(sel)


binder_u4=np.array(binder_u4)



binder_u4=binder_u4[sel]



print(binder_u4)



s=open('binderdata_rounded_t_redosled.txt','w')
s.write(pyalps.plot.convertToText(binder_u4))
s.close()




