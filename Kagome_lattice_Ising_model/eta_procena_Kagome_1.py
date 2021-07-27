# -*- coding: utf-8 -*-
import pyalps
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pyalps.plot
import numpy as np
#prepare the input parameters



data = pyalps.loadMeasurements(pyalps.getResultFiles(prefix='parmkag'), 'Connected Susceptibility')
susc = pyalps.collectXY(data,x='T',y='Connected Susceptibility',foreach=['L'])

red=susc

for d in red:
    d.x=np.around(d.x,3)

fh=open('susc_rounded_t_2D_Ising_Kagome.txt','w')
fh.write(pyalps.plot.convertToText(red))
fh.close()

lvrednost=np.array([q.props['L'] for q in red])
sel=np.argsort(lvrednost)
red=np.array(red)
red=red[sel]

s=open('susc_rounded_t_redosled_2D_Ising_Kagome.txt','w')
s.write(pyalps.plot.convertToText(red))
s.close()

Tc=2.105
a=1.0509

numeratorfig=1

#make a data collapse of the |magnetization| as a function of (T-Tc)/Tc
for two_minus_eta in np.linspace(0.0,3.0,31):
  susc = pyalps.collectXY(data,x='T',y='Connected Susceptibility',foreach=['L'])
  for d in susc:
    d.x -= Tc
    d.x = d.x/Tc
    l = d.props['L']
    d.x = d.x * pow(float(l),a)
    d.y = d.y/pow(float(l),two_minus_eta)  
  plt.figure()
  pyalps.plot.plot(susc)
  plt.xlabel('$L^{a}(T-T_{C})/T_{C}$')
  plt.ylabel(r'$L^{2-\eta}\chi,2-\eta=\gamma/\nu=$ %.6s' % two_minus_eta)
  plt.title(u'2D Izingov model na Kagome rešetki')
  plt.legend(loc='best')
  plt.savefig('figure_Kagome_eta_procena%d.eps'%(numeratorfig),dpi=300)
  numeratorfig+=1

