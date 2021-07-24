# -*- coding: utf-8 -*-
import pyalps
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pyalps.plot
import numpy as np
from scipy import optimize
from scipy import interpolate
import pyalps.fit_wrapper as fw
plt.rcParams.update({'figure.max_open_warning': 0})
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset


data = pyalps.loadMeasurements(pyalps.getResultFiles(prefix='parm7b'),'Binder Cumulant')

numeratorfig=1

for tc in np.linspace(9.0,10.0,101):
    binder_u4 = pyalps.collectXY(data,x='T',y='Binder Cumulant',foreach=['L'])    
    for d in binder_u4:
        d.x -= round(tc,2)
        d.x = d.x/round(tc,2)
    fig, ax = plt.subplots()  
    pyalps.plot.plot(binder_u4)
    plt.xlabel('$t=(T-T_{C})/T_{C}, T_{C}=%.2f$'%(round(tc,2))) 
    plt.ylabel('Binderov kumulant $U_{4}$')
    plt.title(u'3D Izingov model na površinski kubnoj rešetki')
    plt.legend(loc='upper left')
    axins = zoomed_inset_axes(ax, 2.5, loc='upper center') # zoom = 6
    pyalps.plot.plot(binder_u4)
    axins.set_xlim(-0.1, 0.1) # Limit the region for zoom
    axins.set_ylim(1.3, 1.7)
    plt.xticks(visible=True)  # Not present ticks
    plt.yticks(visible=True)
    plt.xlabel("")
    plt.ylabel("")
    plt.grid()
    mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="0.5")
    plt.savefig('figure_FCC_tc_binder_prva_procena%d.eps'%(numeratorfig),dpi=300)
    numeratorfig+=1