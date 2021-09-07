import pyalps
import matplotlib.pyplot as plt
import pyalps.plot
import numpy as np

#prepare the input parameters
parms = []
for s in [0.5,1.0,1.5,2.0]:
  for h in np.linspace(0.0,10.0,101):
    parms.append(
      { 
      'LATTICE'        : "chain lattice", 
      'MODEL'          : "spin",
      'local_S'        : s,
      'T'              : 0.08,
      'J'              : 1 ,
      'THERMALIZATION' : 10000,
      'SWEEPS'         : 100000,
      'L'              : 20,
      'h'              : h
      }
  )

#write the input file and run the simulation
input_file = pyalps.writeInputFiles('parmHmagS',parms)
res = pyalps.runApplication('dirloop_sse',input_file,Tmin=5)

#load the magnetization and collect it as function of field h
data = pyalps.loadMeasurements(pyalps.getResultFiles(prefix='parmHmagS'),'Magnetization Density')
magnetization = pyalps.collectXY(data,x='h',y='Magnetization Density', foreach=['local_S'])

#make plot
plt.figure()
pyalps.plot.plot(magnetization)
plt.xlabel('$h$')
plt.ylabel('Magnetizacija')
plt.ylim(0.0,2.1)
plt.title('Kvantni Hajzenbergov lanac (Quantum Heisenberg chain)')
plt.legend(loc='best')
plt.savefig("magnetization_heisenberg_chain_S.eps",dpi=300)
