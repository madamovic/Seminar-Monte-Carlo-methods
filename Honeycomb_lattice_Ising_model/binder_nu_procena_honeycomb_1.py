# -*- coding: utf-8 -*-
import pyalps
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pyalps.plot
import numpy as np
import pyalps.fit_wrapper as fw
plt.rcParams.update({'figure.max_open_warning': 0})


data = pyalps.loadMeasurements(pyalps.getResultFiles(prefix='parm7a'),'Binder Cumulant')

numeratorfig=1

tc=1.504 #procena

for a in np.linspace(0.0,1.5,16):
    binder_u4 = pyalps.collectXY(data,x='T',y='Binder Cumulant',foreach=['L'])    
    for d in binder_u4:
        d.x -= tc
        d.x = d.x/tc
        l=d.props['L']
        d.x=d.x*pow(float(l),a)
    fig, ax = plt.subplots()  
    pyalps.plot.plot(binder_u4)
    plt.xlabel('$L^a(T-T_c)/T_c, T_c=%.3f,a=%.2f$'%(tc,round(a,3))) 
    plt.ylabel('Binderov kumulant $U_{4}$')
    plt.title(u'2D Izingov model na honeycomb rešetki')
    plt.legend(loc='upper left')
    plt.savefig('figure_honeycomb_nu_binder_procena%d.eps'%(numeratorfig),dpi=300)
    numeratorfig+=1

