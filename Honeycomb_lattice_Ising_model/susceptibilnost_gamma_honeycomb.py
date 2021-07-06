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
    for t in np.linspace(1.4,1.6,21):
        parms.append(
            { 
              'LATTICE'        : "honeycomb lattice", 
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
input_file = pyalps.writeInputFiles('parm1',parms)
pyalps.runApplication('spinmc',input_file,Tmin=5)
# use the following instead if you have MPI
#pyalps.runApplication('spinmc',input_file,Tmin=5,MPI=4)

pyalps.evaluateSpinMC(pyalps.getResultFiles(prefix='parm1'))

#load the susceptibility and collect it as function of temperature T
data = pyalps.loadMeasurements(pyalps.getResultFiles(prefix='parm1'),'Connected Susceptibility')

connected_susc = pyalps.collectXY(data,x='T',y='Connected Susceptibility',foreach=['L'])

 
#make a fit of the connected susceptibility as a function of L:
cs_mean=[]
for q in connected_susc:
    cs_mean.append(np.array([d.mean for d in q.y]))


peak_cs = pyalps.DataSet()
peak_cs.props = pyalps.dict_intersect([q.props for q in connected_susc])
peak_cs.y = np.array([np.max(q) for q in cs_mean])
peak_cs.x = np.array([q.props['L'] for q in connected_susc])
# 



sel = np.argsort(peak_cs.x)


peak_cs.y = peak_cs.y[sel]
peak_cs.x = peak_cs.x[sel]

from scipy import optimize

def test_funk(x,a,b):
    return a*x**b

params,params_covariance=optimize.curve_fit(test_funk,peak_cs.x,peak_cs.y)

print(params[0],params[1])
print(params_covariance)
print(np.sqrt(np.diag(params_covariance)))


# 
plt.figure()
plt.scatter(peak_cs.x,peak_cs.y,label='Podaci',color='b')
plt.plot(peak_cs.x,test_funk(peak_cs.x,params[0],params[1]),color='r')
plt.xlabel('$L$')
plt.ylabel(r'Susceptibilnost $\chi(T_{C})=\chi^{max}$')
plt.title(ur'2D Izingov model na honeycomb rešetki, $\gamma/\nu =$ %.10s' % params[1])
plt.savefig("figure_gamma_over_nu_honeycomb.eps",dpi=300)