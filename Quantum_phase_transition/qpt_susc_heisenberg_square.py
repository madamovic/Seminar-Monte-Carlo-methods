import pyalps
import matplotlib.pyplot as plt
import pyalps.plot
import numpy as np

parms = []
for j2 in [0.,1.]:
    for t in np.linspace(0.1,4.0,400):
        parms.append(
            { 
              'LATTICE'        : "coupled ladders", 
              'local_S'        : 0.5,
              'ALGORITHM'      : 'loop',
              'SEED'           : 0,
              'T'              : t,
              'J0'             : 1 ,
              'J1'             : 1,
              'J2'             : j2,
              'THERMALIZATION' : 5000,
              'SWEEPS'         : 50000, 
              'MODEL'          : "spin",
              'L'              : 8,
              'W'              : 8
            }
    )
    
#write the input file and run the simulation
input_file = pyalps.writeInputFiles('parm8a',parms)
pyalps.runApplication('loop',input_file)

data = pyalps.loadMeasurements(pyalps.getResultFiles(prefix='parm8a'),['Staggered Susceptibility','Susceptibility'])
susc1=pyalps.collectXY(data,x='T',y='Susceptibility', foreach=['J2'])

plt.figure()
pyalps.plot.plot(susc1)
plt.xlabel(r'$T$')
plt.ylabel(r'$\chi$')
plt.legend()
plt.savefig("qpt_susc.eps",dpi=300)
