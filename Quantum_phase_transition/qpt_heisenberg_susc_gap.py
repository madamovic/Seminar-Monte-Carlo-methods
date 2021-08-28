# -*- coding: utf-8 -*-
import pyalps
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import pyalps.plot
import numpy as np

start=0.1
stop=4.0
step=0.01

#prepare the input parameters
parms = []
for j2 in [0.0]:
    for t in np.arange(start,stop,step):
        parms.append(
            { 
              'LATTICE'        : "coupled ladders", 
              'local_S'        : 0.5,
              'ALGORITHM'      : 'loop',
              'SEED'           : 0,
              'T'              : t,
              'J0'             : 1 ,
              'J1'             : 1,
              'J2'             : j2,
              'THERMALIZATION' : 5000,
              'SWEEPS'         : 50000, 
              'MODEL'          : "spin",
              'L'              : 8,
              'W'              : 8
            }
    )
    
#write the input file and run the simulation
input_file = pyalps.writeInputFiles('parm8a',parms)
pyalps.runApplication('loop',input_file)

data = pyalps.loadMeasurements(pyalps.getResultFiles(prefix='parm8a'),['Staggered Susceptibility','Susceptibility'])
susc=pyalps.collectXY(data,x='T',y='Susceptibility', foreach=['J2'])


f = open('susc_Heisenberg_square_ladder.txt','w')
f.write(pyalps.plot.convertToText(susc))
f.close()



file=open('susc_Heisenberg_square_ladder.txt')

file_data=np.loadtxt(file,usecols=(0,1))


x=file_data[:,0]
y=file_data[:,1]


listax=x[:int((1-start)/step)+1]
listay=y[:int((1-start)/step)+1]


def test_funk(x,a,b):
    return (a/np.sqrt(x))*np.exp(-b/x)

params,params_covariance=curve_fit(test_funk,listax,listay)

print(params[0],params[1])
print(np.sqrt(np.diag(params_covariance)))


plt.figure()
plt.scatter(listax,listay,label='Podaci',color='b')
plt.plot(listax,test_funk(listax,params[0],params[1]),color='r',label='Rezultat fitovanja')
plt.xlabel('$T$')
plt.ylabel(u'Susceptibilnost')
plt.title(ur'Hajzenbergov model na kvadratnoj rešetki (ladder), $\Delta=$ %.10s' % params[1])
plt.legend(loc='best')
plt.savefig("susc_Heisenberg_square_ladder.eps",dpi=300)
