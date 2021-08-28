import pyalps
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.offsetbox import AnchoredText

numerator=1

for t in [1.0,1.5,2.0,2.2,2.26,2.3,3.0,3.5,4.0]:
	parms = [{
	'LATTICE'         : "square lattice",          
  	'MODEL'           : "Ising",
  	'L'               : 8,
  	'J'               : 1.,
  	'T'               : t,
  	'THERMALIZATION'  : 1000000,
  	'SWEEPS'          : 1000000,
  	'UPDATE'		  : "local"
	}]
	input_file = pyalps.writeInputFiles('parmtemps',parms)
	pyalps.runApplication('spinmc', input_file, Tmin=10, writexml=True)
	files = pyalps.getResultFiles(prefix='parmtemps')
	ts_M = pyalps.loadTimeSeries(files[0], '|Magnetization|')
	vrednost=pyalps.checkSteadyState(outfile=files[0], observable='|Magnetization|')["value"]
	boja='red'
	if vrednost==1:
		boja='green'
	plt.figure()
	plt.plot(ts_M)
	plt.text(len(ts_M)-5,max(ts_M), str(vrednost), bbox=dict(facecolor=boja, alpha=0.5))
	plt.savefig("timemag_local_%d.eps"%(numerator),dpi=300)
	numerator+=1



