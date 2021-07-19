# -*- coding: utf-8 -*-
import numpy as np
from intersections import *


file=open('binderdata_rounded_t_redosled_3D_Ising_BCC.txt')

file_data=np.loadtxt(file,usecols=(0,1))

x=file_data[:,0]
y=file_data[:,1]

llista = [4,6,8,10,12] #lattice velicina
n=91 #koraci

for i in range(0,len(llista)):
    exec("x%d = x[i*n:i*n+n]" % (llista[i]));

for j in range(0,len(llista)):
    exec("y%d = y[j*n:j*n+n]" % (llista[j]));

tstart=6.301
tstop=6.34

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    xintercept1, yintercept1 = intersection(x4, y4, x6, y6)
    xintercept2, yintercept2 = intersection(x4, y4, x8, y8)
    xintercept3, yintercept3 = intersection(x4, y4, x10, y10)
    xintercept4, yintercept4 = intersection(x4, y4, x12, y12)
    listaintersceptsx=[]
    listaintersceptsy=[]
    for i in range(0,len(xintercept1)):
    	if tstart<= xintercept1[i] <= tstop:
    		listaintersceptsx.append(xintercept1[i])
    		listaintersceptsy.append(yintercept1[i])

    for i in range(0,len(xintercept2)):
    	if tstart<= xintercept2[i] <= tstop:
    		listaintersceptsx.append(xintercept2[i])
    		listaintersceptsy.append(yintercept2[i])

    for i in range(0,len(xintercept3)):
    	if tstart<= xintercept3[i] <= tstop:
    		listaintersceptsx.append(xintercept3[i])
    		listaintersceptsy.append(yintercept3[i])

    for i in range(0,len(xintercept4)):
        if tstart<= xintercept4[i] <= tstop:
            listaintersceptsx.append(xintercept4[i])
            listaintersceptsy.append(yintercept4[i])




lodnosi=[6.0/4.0,8.0/4.0,10.0/4.0,12.0/4.0]

xosa=1/np.log(lodnosi)

from scipy import optimize

def test_funk(x,a,b):
    return a*x+b

params, params_cov=optimize.curve_fit(test_funk,xosa,listaintersceptsx)

print(params[0],params[1])
print(np.sqrt(np.diag(params_cov)))


plt.figure()
plt.scatter(xosa,listaintersceptsx,label='Podaci',color='blue')
plt.plot(xosa,test_funk(xosa,params[0],params[1]),label='Linear fit',color='black')
plt.xlabel('1/ln(b)')
plt.ylabel('$T_{c}$')
plt.title(u'3D Izingov model na zapreminski centriranoj kubnoj rešetki')
plt.savefig("presek_kumulanata_BCC_tc_lnL.eps",dpi=300)
plt.show()
    
    
    
