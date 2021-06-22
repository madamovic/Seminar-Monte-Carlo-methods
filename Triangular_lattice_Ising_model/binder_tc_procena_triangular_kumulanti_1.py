# -*- coding: utf-8 -*-
import numpy as np
from intersections import *


file=open('binderdata_rounded_t_redosled_2D_Ising_triangular.txt')

file_data=np.loadtxt(file,usecols=(0,1))


x=file_data[:,0]
y=file_data[:,1]



llista = [8,16,24,32,40] #lattice velicina
n=61 #koraci




for i in range(0,len(llista)):
    exec("x%d = x[i*n:i*n+n]" % (llista[i]));

for j in range(0,len(llista)):
    exec("y%d = y[j*n:j*n+n]" % (llista[j]));


tstart=3.61
tstop=3.64

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    xintercept1, yintercept1 = intersection(x8, y8, x16, y16)
    xintercept2, yintercept2 = intersection(x8, y8, x24, y24)
    xintercept3, yintercept3 = intersection(x8, y8, x32, y32)
    xintercept4, yintercept4 = intersection(x8, y8, x32, y40)
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



lodnosi=[16.0/8.0,24.0/8.0,32.0/8.0,40.0/8.0]

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
plt.title(u'2D Izingov model na trougaonoj rešetki')
plt.savefig("presek_kumulanata_triangular_tc_lnL.eps",dpi=300)
plt.show()
    
    
    
