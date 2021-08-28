import pyalps
import matplotlib.pyplot as plt

# Set up a python list of parameters (python) dictionaries:
parms = [{
  'LATTICE'         : "square lattice",          
  'MODEL'           : "Ising",
  'L'               : 24,
  'J'               : 1.,
  'T'               : 2.26919,
  'THERMALIZATION'  : 10000000,
  'SWEEPS'          : 1000000,
  'UPDATE'			: "local"
}]


input_file = pyalps.writeInputFiles('parm1e',parms)

pyalps.runApplication('spinmc', input_file, Tmin=10, writexml=True)

files = pyalps.getResultFiles(prefix='parm1e')

print(pyalps.checkSteadyState(outfile=files[0], observable='|Magnetization|', confidenceInterval=0.80))
print(pyalps.checkSteadyState(outfile=files[0], observable='Energy', confidenceInterval=0.80))


