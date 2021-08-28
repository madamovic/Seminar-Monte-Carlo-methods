import pyalps
import matplotlib.pyplot as plt

# Set up a python list of parameters (python) dictionaries:
parms = [{
  'LATTICE'         : "square lattice",          
  'MODEL'           : "Ising",
  'L'               : 32,
  'J'               : 1.,
  'T'               : 2.26919,
  'THERMALIZATION'  : 10000,
  'SWEEPS'          : 50000,
  'UPDATE'			: "local"
}]


input_file = pyalps.writeInputFiles('parm1b',parms)

pyalps.runApplication('spinmc', input_file, Tmin=10, writexml=True)

files = pyalps.getResultFiles(prefix='parm1b')

ts_M = pyalps.loadTimeSeries(files[0], '|Magnetization|');

plt.figure()
plt.plot(ts_M)
plt.savefig("timemag2.eps",dpi=300)


print(pyalps.checkSteadyState(outfile=files[0], observable='|Magnetization|', confidenceInterval=0.95))
print(pyalps.checkSteadyState(outfile=files[0], observable='Energy', confidenceInterval=0.95))


