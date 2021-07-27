# -*- coding: utf-8 -*-
import pyalps
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pyalps.plot
import numpy as np
import pyalps.fit_wrapper as fw

#prepare the input parameters
parms = []
for l in [8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40]:
    for t in np.linspace(2.0,2.5,11):
        parms.append(
            { 
              'LATTICE'        : "Kagome lattice", 
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
input_file = pyalps.writeInputFiles('parm2',parms)
pyalps.runApplication('spinmc',input_file,Tmin=5)
# use the following instead if you have MPI
#pyalps.runApplication('spinmc',input_file,Tmin=5,MPI=4)

pyalps.evaluateSpinMC(pyalps.getResultFiles(prefix='parm2'))

#load the susceptibility and collect it as function of temperature T
data = pyalps.loadMeasurements(pyalps.getResultFiles(prefix='parm2'), 'Specific Heat')
spec_heat = pyalps.collectXY(data,x='T',y='Specific Heat',foreach=['L'])


sh_mean=[]
for q in spec_heat:
    sh_mean.append(np.array([d.mean for d in q.y]))

peak_sh = pyalps.DataSet()
peak_sh.props = pyalps.dict_intersect([q.props for q in spec_heat])
peak_sh.y = np.array([np.max(q) for q in sh_mean])
peak_sh.x = np.array([q.props['L'] for q in spec_heat])
 
sel = np.argsort(peak_sh.x)
peak_sh.y = peak_sh.y[sel]
peak_sh.x = peak_sh.x[sel]

from scipy import optimize

def test_funk(x,a,b):
    return a*x**b

params,params_covariance=optimize.curve_fit(test_funk,peak_sh.x,peak_sh.y)

print(params[0],params[1])
print(params_covariance)
print(np.sqrt(np.diag(params_covariance)))

plt.figure()
plt.scatter(peak_sh.x,peak_sh.y,label='Podaci',color='b')
plt.plot(peak_sh.x,test_funk(peak_sh.x,params[0],params[1]),color='r')
plt.xlabel('$L$')
plt.ylabel(u'Specifična toplota $C_{V}(T_c)=C_{V}^{max}$')
plt.title(ur'2D Izingov model na Kagome rešetki, $\alpha/\nu=$ %.10s' % params[1])
plt.savefig("figure_alpha_over_nu_Kagome.eps",dpi=300)


