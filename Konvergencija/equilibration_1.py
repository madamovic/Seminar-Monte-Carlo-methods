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

# Write into XML input file:
input_file = pyalps.writeInputFiles('parm1a',parms)

# and run the application spinmc:
pyalps.runApplication('spinmc', input_file, Tmin=10, writexml=True)

# We first get the list of all hdf5 result files via:
files = pyalps.getResultFiles(prefix='parm1a')

# and then extract, say the timeseries of the |Magnetization| measurements:
ts_M = pyalps.loadTimeSeries(files[0], '|Magnetization|');

# We can then visualize graphically:
plt.figure()
plt.plot(ts_M)
plt.savefig("timemag1.eps",dpi=300)

# ALPS Python provides a convenient tool to check whether a measurement observable(s) has (have) reached steady state equilibrium.
#
# Here is one example:
print(pyalps.checkSteadyState(outfile=files[0], observable='|Magnetization|'))
print(pyalps.checkSteadyState(outfile=files[0], observable='Energy'))


