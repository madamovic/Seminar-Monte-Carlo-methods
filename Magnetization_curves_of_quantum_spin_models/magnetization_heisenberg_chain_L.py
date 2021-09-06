import pyalps
import matplotlib.pyplot as plt
import pyalps.plot
import numpy as np

#prepare the input parameters
parms = []
for l in [20,40,60,80,100]:
  for h in np.linspace(0.0,5.0,51):
    parms.append(
      { 
      'LATTICE'        : "chain lattice", 
      'MODEL'          : "spin",
      'local_S'        : 0.5,
      'T'              : 0.08,
      'J'              : 1 ,
      'THERMALIZATION' : 10000,
      'SWEEPS'         : 100000,
      'L'              : l,
      'h'              : h
      }
  )

#write the input file and run the simulation
input_file = pyalps.writeInputFiles('parmHmagL',parms)
res = pyalps.runApplication('dirloop_sse',input_file,Tmin=5)

#load the magnetization and collect it as function of field h
data = pyalps.loadMeasurements(pyalps.getResultFiles(prefix='parmHmagL'),'Magnetization Density')
magnetization = pyalps.collectXY(data,x='h',y='Magnetization Density', foreach=['L'])

#make plot
plt.figure()
pyalps.plot.plot(magnetization)
plt.xlabel('$h$')
plt.ylabel('Magnetizacija')
plt.ylim(0.0,0.6)
plt.title('Kvantni Hajzenbergov lanac (Quantum Heisenberg chain)')
plt.legend(loc='best')
plt.savefig("magnetization_heisenberg_chain_L.eps",dpi=300)
