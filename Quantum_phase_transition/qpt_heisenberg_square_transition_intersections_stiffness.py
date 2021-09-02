import numpy as np

from intersections import *

file=open('stiffness_rounded_heisenberg_redosled.txt')

file_data=np.loadtxt(file,usecols=(0,1))


x=file_data[:,0]
y=file_data[:,1]

llista = [8,10,12,16]#lattice velicina
n=101 #koraci

for i in range(0,len(llista)):
    exec("x%d = x[i*n:i*n+n]" % (llista[i]));

for j in range(0,len(llista)):
    exec("y%d = y[j*n:j*n+n]" % (llista[j]));

tstart=0.30
tstop=0.35

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    xintercept1, yintercept1 = intersection(x8, y8, x10, y10)
    xintercept2, yintercept2 = intersection(x8, y8, x12, y12)
    xintercept3, yintercept3 = intersection(x8, y8, x16, y16)

    xintercept4, yintercept4 = intersection(x10, y10, x12, y12)
    xintercept5, yintercept5 = intersection(x10, y10, x16, y16)
    xintercept6, yintercept6 = intersection(x12, y12, x16, y16)

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
    plt.plot(x8, y8, c='r')
    plt.plot(x10, y10, c='g')
    plt.plot(x12, y12, c='b')
    plt.plot(x16, y16, c='purple')
    plt.plot(listaintersceptsx, listaintersceptsy, '*k')
    plt.xlabel(r'$J_{2}$')
    plt.ylabel(r'$\rho_{s}L$')
    plt.savefig("presek_kumulanata_heisenbeg_stiffness.eps",dpi=300)
    plt.show()

    for i in range(0,len(listaintersceptsx)):
		print(listaintersceptsx[i])

    textfile = open("kumulanti_stiffness_preseci_pojedinacni.txt", "w")

    for element in listaintersceptsx:
        textfile.write(str(element) + "\n")
    textfile.close()