# -*- coding: utf-8 -*-
import pyalps
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pyalps.plot
import numpy as np


parms = []
for l in [8,10,12,16]:
    for j2 in np.linspace(0.1,0.6,101):
        parms.append(
            { 
              'LATTICE'        : "coupled ladders", 
              'local_S'        : 0.5,
              'ALGORITHM'      : 'loop',
              'SEED'           : 0,
              'BETA'           : 2*l,
              'J0'             : 1 ,
              'J1'             : 1,
              'J2'             : j2,
              'THERMALIZATION' : 5000,
              'SWEEPS'         : 50000, 
              'MODEL'          : "spin",
              'L'              : l,
              'W'              : l
            }
    )
    
#write the input file and run the simulation
input_file = pyalps.writeInputFiles('parme',parms)
pyalps.runApplication('loop',input_file)


data = pyalps.loadMeasurements(pyalps.getResultFiles(prefix='parme'),['Staggered Susceptibility','Susceptibility'])
susc=pyalps.collectXY(data,x='J2',y='Staggered Susceptibility', foreach=['L'])

red=susc

for d in red:
    d.x=np.around(d.x,3)

lvrednost=np.array([q.props['L'] for q in red])
sel=np.argsort(lvrednost)
red=np.array(red)
red=red[sel]

s=open('susc_rounded_heisenberg_redosled.txt','w')
s.write(pyalps.plot.convertToText(red))
s.close()

from scipy import interpolate


file=open('susc_rounded_heisenberg_redosled.txt')

file_data=np.loadtxt(file,usecols=(0,1))

x=file_data[:,0]
y=file_data[:,1]
llista = [8,10,12,16]
n=101

for i in range(0,len(llista)):
    exec("x%d = x[i*n:i*n+n]" % (llista[i]));

for j in range(0,len(llista)):
    exec("y%d = y[j*n:j*n+n]" % (llista[j]));

#funk = interpolate.interp1d(x, y)

for k in range(0,len(llista)):
    exec("funk%d = interpolate.interp1d(x%d, y%d)" % (llista[k],llista[k],llista[k]));
    

lista=[]
jc=0.32

from scipy import optimize

for m in range(0,len(llista)):
  exec("rez=funk%d(jc)"%llista[m])
  lista.append(rez)

def test_funk(x,a,b):
    return a*x**b

params,params_covariance=optimize.curve_fit(test_funk,llista,lista)

print(params[0],params[1])
print(np.sqrt(np.diag(params_covariance)))

plt.figure()
plt.scatter(llista,lista,label='Podaci',color='b')
plt.plot(llista,test_funk(llista,params[0],params[1]),label='Fit',color='r')
plt.xlabel('$L$')
plt.ylabel(r'$\chi_{s}(J_{2}^{C})$')
plt.title(r'$2-\eta=$ %.13s' % (params[1]))
plt.legend(loc='best')
plt.savefig("figure_eta_heisenberg.eps",dpi=300)
