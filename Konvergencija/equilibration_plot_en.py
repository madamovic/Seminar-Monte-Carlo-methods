import pyalps
import matplotlib.pyplot as plt
import numpy as np


lista_da=[]
lista_ne=[]
temp_da=[]
temp_ne=[]
nth_da=[]
nth_ne=[]


trenutni=1

for nth in np.arange(0,1001000,50000):
	for t in np.linspace(0.0,4.0,41):
		print("******************")
		print("Trenutno izvrsava "+str(trenutni)+"/"+str(len(np.arange(0,1001000,50000))*len(np.linspace(0.0,4.0,41))))
		print("******************")
		parms = [{
		'LATTICE'         : "square lattice",          
		'MODEL'           : "Ising",
  		'L'               : 8,
  		'J'               : 1.,
  		'T'               : t,
  		'THERMALIZATION'  : nth,
  		'SWEEPS'          : 1000000,
  		'UPDATE'          : "cluster"
		}]
		input_file = pyalps.writeInputFiles('parmPen',parms)
		pyalps.runApplication('spinmc', input_file, Tmin=10, writexml=True)
		files = pyalps.getResultFiles(prefix='parmPen')

		vrednost=int(pyalps.checkSteadyState(outfile=files[0], observable='Energy')["value"])

		trenutni+=1

		if vrednost==0:
			lista_ne.append(vrednost)
			temp_ne.append(t)
			nth_ne.append(nth)
		else:
			lista_da.append(vrednost)
			temp_da.append(t)
			nth_da.append(nth)


plt.figure()
plt.scatter(nth_ne,temp_ne,color='red',label="not steady state")
plt.scatter(nth_da,temp_da,color= 'green',label='steady state')
plt.axhline(y=2.26919, color='b', linestyle='--')
plt.xlabel("$N_{TH}$")
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.legend(loc='best')
plt.savefig("equilibration_en_plot.eps",dpi=300)