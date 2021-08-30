import pyalps
import matplotlib.pyplot as plt
import pyalps.plot
import numpy as np

numerator=1

for s in [0.5,1.0,1.5,2.0,2.5,3.0]:
  parms = []
  for j2 in [0.,1.]:
    for t in np.linspace(0.1,4.0,400):
      parms.append(
      { 
      'LATTICE'        : "coupled ladders", 
      'local_S'        : s,
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
      })
  input_file = pyalps.writeInputFiles('parmS',parms)
  pyalps.runApplication('loop',input_file)

  data = pyalps.loadMeasurements(pyalps.getResultFiles(prefix='parmS'),['Staggered Susceptibility','Susceptibility'])
  susc=pyalps.collectXY(data,x='T',y='Susceptibility', foreach=['J2'])

  plt.figure()
  pyalps.plot.plot(susc)
  plt.xlabel(r'$T$')
  plt.ylabel(r'$\chi$')
  plt.legend()
  plt.savefig("qpt_susc_spin_%d.eps"%(numerator),dpi=300)
  numerator+=1
