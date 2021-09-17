# -*- coding: utf-8 -*
import numpy as np
from intersections import *


file=open('redosled_rad_jedan.txt')

file_data=np.loadtxt(file,usecols=(0,1))

x=file_data[:,0]
y=file_data[:,1]

llista = [4,6,8,10,12,14,16]#lattice velicina
n=31 #koraci

for i in range(0,len(llista)):
    exec("x%d = x[i*n:i*n+n]" % (llista[i]));

for j in range(0,len(llista)):
    exec("y%d = y[j*n:j*n+n]" % (llista[j]));

tstart=0.98
tstop=1.08

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    xintercept1, yintercept1 = intersection(x4, y4, x6, y6)
    xintercept2, yintercept2 = intersection(x4, y4, x8, y8)
    xintercept3, yintercept3 = intersection(x4, y4, x10, y10)
    xintercept4, yintercept4 = intersection(x4, y4, x12, y12)
    xintercept5, yintercept5 = intersection(x4, y4, x14, y14)
    xintercept6, yintercept6 = intersection(x4, y4, x16, y16)
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

    for i in range(0,len(xintercept5)):
    	if tstart<= xintercept5[i] <= tstop:
    		listaintersceptsx.append(xintercept5[i])
    		listaintersceptsy.append(yintercept5[i])

    for i in range(0,len(xintercept6)):
    	if tstart<= xintercept6[i] <= tstop:
    		listaintersceptsx.append(xintercept6[i])
    		listaintersceptsy.append(yintercept6[i])



plt.figure()
plt.plot(x4, y4, c='r')
plt.plot(x6, y6, c='g')
plt.plot(x8, y8, c='b')
plt.plot(x10, y10, c='yellow')
plt.plot(x12, y12, c='purple')
plt.plot(x14, y14, c='c')
plt.plot(x16, y16, c='m')
plt.plot(listaintersceptsx, listaintersceptsy, '*k')
plt.xlim(0.98,1.1)
plt.ylim(0,3)
plt.xlabel('T')
plt.ylabel(r'$\rho_{s}L$')
plt.savefig("preseci_rad_jedan.eps",dpi=300)
plt.show()


for i in range(0,len(listaintersceptsx)):
    print(listaintersceptsx[i])

textfile = open("preseci_rad_jedan_pojedinacni.txt", "w")

for element in listaintersceptsx:
    textfile.write(str(element) + "\n")
textfile.close()