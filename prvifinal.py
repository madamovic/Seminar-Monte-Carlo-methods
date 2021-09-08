import pyalps
import matplotlib.pyplot as plt
import pyalps.plot

parms = []
for t in [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0,1.2,1.4,1.6,1.8,2.0,2.2,2.4,2.6,2.8,3.0,3.2]:
   parms.append(
       { 
         'LATTICE'        : "square lattice", 
         'T'              : t,
         'J'              : 1 ,
         'THERMALIZATION' : 1000,
         'SWEEPS'         : 100000,
         'UPDATE'         : "cluster",
         'MODEL'          : "Ising",
         'L'              : 8
       }
   )

input_file = pyalps.writeInputFiles('parm1',parms)

pyalps.runApplication('spinmc',input_file,Tmin=5,writexml=True)

#pyalps.runApplication('spinmc',input_file,Tmin=5,writexml=True,MPI=4)

result_files = pyalps.getResultFiles(prefix='parm1')
data = pyalps.loadMeasurements(result_files,['|Magnetization|','Magnetization^2'])

plotdata = pyalps.collectXY(data,'T','|Magnetization|')

plt.figure()
pyalps.plot.plot(plotdata)
plt.xlim(0,3)
plt.ylim(0,1)
plt.title('Ising model')
plt.show()