# -*- coding: utf-8 -*-
import pyalps
import matplotlib.pyplot as plt
import pyalps.plot

#prepare the input parameters
parms = []
for l in [2,4,8,16,32,48,64]:
    parms.append(
        { 
          'LATTICE'        : "square lattice", 
          'T'              : 2.0,
          'J'              : 1 ,
          'THERMALIZATION' : 50000,
          'SWEEPS'         : 50000,
          'UPDATE'         : "local",
          'MODEL'          : "Ising",
          'L'              : l
        }
    )

#write the input file and run the simulation
input_file = pyalps.writeInputFiles('loctemp3',parms)
pyalps.runApplication('spinmc',input_file,Tmin=5)

#load the binning analysis for the absolute value of the magnetization
binning = pyalps.loadBinningAnalysis(pyalps.getResultFiles(prefix='loctemp3'),'|Magnetization|')
binning = pyalps.flatten(binning)

#make one plot with all data
for dataset in binning:
    dataset.props['label'] = 'L='+str(dataset.props['L'])

plt.figure()
plt.xlabel('bining nivo')
plt.ylabel(u'Greška za magnetizaciju')
plt.title(u'Bining analiza za 2D Izingov model na kvadratnoj rešetki, local updates')
pyalps.plot.plot(binning)
plt.legend(loc="best")
plt.savefig("bining_local_temp_3.eps",dpi=300)


