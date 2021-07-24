# -*- coding: utf-8 -*-
import pyalps
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pyalps.plot
import numpy as np
#prepare the input parameters

parms = []
for l in [4,6,8,10,12,14,16]:
    for t in np.linspace(9.0,10.0,21):
        parms.append(
            { 
              'LATTICE'        : "fcc",
              'LATTICE_LIBRARY' : "fcc.xml", 
              'T'              : t,
              'J'              : 1 ,
              'THERMALIZATION' : 100000,
              'SWEEPS'         : 1000000,
              'UPDATE'         : "cluster",
              'MODEL'          : "Ising",
              'L'              : l
            }
    )

#write the input file and run the simulation
input_file = pyalps.writeInputFiles('parmFCC',parms)
pyalps.runApplication('spinmc',input_file,Tmin=5)
# use the following instead if you have MPI
#pyalps.runApplication('spinmc',input_file,Tmin=5,MPI=4)

pyalps.evaluateSpinMC(pyalps.getResultFiles(prefix='parmFCC'))

data = pyalps.loadMeasurements(pyalps.getResultFiles(prefix='parmFCC'), '|Magnetization|')
magnetization_abs = pyalps.collectXY(data,x='T',y='|Magnetization|',foreach=['L'])

red=magnetization_abs

for d in red:
    d.x=np.around(d.x,3)

fh=open('mag_rounded_t_3D_Ising_FCC.txt','w')
fh.write(pyalps.plot.convertToText(red))
fh.close()

lvrednost=np.array([q.props['L'] for q in red])
sel=np.argsort(lvrednost)
red=np.array(red)
red=red[sel]

s=open('mag_rounded_t_redosled_3D_Ising_FCC.txt','w')
s.write(pyalps.plot.convertToText(red))
s.close()

Tc=9.784
a=1.694

numeratorfig=1

#make a data collapse of the |magnetization| as a function of (T-Tc)/Tc
for beta_over_nu in np.linspace(0.0,1.6,17):
  magnetization_abs = pyalps.collectXY(data,x='T',y='|Magnetization|',foreach=['L'])
  for d in magnetization_abs:
    d.x -= Tc
    d.x = d.x/Tc
    l = d.props['L']
    d.x = d.x * pow(float(l),a)
    d.y = d.y / pow(float(l),-beta_over_nu)   
  plt.figure()
  pyalps.plot.plot(magnetization_abs)
  plt.xlabel('$L^{a}(T-T_{C})/T_{C}$')
  plt.ylabel(r'Magnetizacija $|m|L^{-\beta/\nu}, \beta/\nu=$ %.6s' % beta_over_nu)
  plt.title(u'3D Izingov model na površinski centriranoj kubnoj rešetki')
  plt.legend(loc='best')
  plt.savefig('figure_FCC_beta_nu_binder_procena%d.eps'%(numeratorfig),dpi=300)
  numeratorfig+=1

