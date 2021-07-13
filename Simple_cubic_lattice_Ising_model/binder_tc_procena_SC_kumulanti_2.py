import numpy as np
from intersections import *


file=open('binderdata_rounded_t_redosled_3D_Ising_SC.txt')

file_data=np.loadtxt(file,usecols=(0,1))

x=file_data[:,0]
y=file_data[:,1]

llista = [4,8,10,12,14,16] #lattice velicina
n=71 #koraci

for i in range(0,len(llista)):
    exec("x%d = x[i*n:i*n+n]" % (llista[i]));

for j in range(0,len(llista)):
    exec("y%d = y[j*n:j*n+n]" % (llista[j]));

tstart=4.49
tstop=4.52

if __name__ == '__main__':
    import matplotlib.pyplot as plt
    xintercept1, yintercept1 = intersection(x4, y4, x8, y8)
    xintercept2, yintercept2 = intersection(x4, y4, x10, y10)
    xintercept3, yintercept3 = intersection(x4, y4, x12, y12)
    xintercept4, yintercept4 = intersection(x4, y4, x14, y14)
    xintercept5, yintercept5 = intersection(x4, y4, x16, y16)

    xintercept6, yintercept6 = intersection(x8, y8, x10, y10)
    xintercept7, yintercept7 = intersection(x8, y8, x12, y12)
    xintercept8, yintercept8 = intersection(x8, y8, x14, y14)
    xintercept9, yintercept9 = intersection(x8, y8, x16, y16)

    xintercept10, yintercept10 = intersection(x10, y10, x12, y12)
    xintercept11, yintercept11 = intersection(x10, y10, x14, y14)
    xintercept12, yintercept12 = intersection(x10, y10, x16, y16)

    xintercept13, yintercept13 = intersection(x12, y12, x14, y14)
    xintercept14, yintercept14 = intersection(x12, y12, x16, y16)
    xintercept15, yintercept15 = intersection(x14, y14, x16, y16)

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

    for i in range(0,len(xintercept7)):
    	if tstart<= xintercept7[i] <= tstop:
    		listaintersceptsx.append(xintercept7[i])
    		listaintersceptsy.append(yintercept7[i])

    for i in range(0,len(xintercept8)):
    	if tstart<= xintercept8[i] <= tstop:
    		listaintersceptsx.append(xintercept8[i])
    		listaintersceptsy.append(yintercept8[i])

    for i in range(0,len(xintercept9)):
    	if tstart<= xintercept9[i] <= tstop:
    		listaintersceptsx.append(xintercept9[i])
    		listaintersceptsy.append(yintercept9[i])

    for i in range(0,len(xintercept10)):
    	if tstart<= xintercept10[i] <= tstop:
    		listaintersceptsx.append(xintercept10[i])
    		listaintersceptsy.append(yintercept10[i])
	
	for i in range(0,len(xintercept11)):
		if tstart<= xintercept11[i] <= tstop:
			listaintersceptsx.append(xintercept11[i])
			listaintersceptsy.append(yintercept11[i])

   	for i in range(0,len(xintercept12)):
   		if tstart<= xintercept12[i] <= tstop:
   			listaintersceptsx.append(xintercept12[i])
   			listaintersceptsy.append(yintercept12[i])

   	for i in range(0,len(xintercept13)):
   		if tstart<= xintercept13[i] <= tstop:
   			listaintersceptsx.append(xintercept13[i])
   			listaintersceptsy.append(yintercept13[i])


   	for i in range(0,len(xintercept14)):
   		if tstart<= xintercept14[i] <= tstop:
   			listaintersceptsx.append(xintercept14[i])
   			listaintersceptsy.append(yintercept14[i])


    for i in range(0,len(xintercept15)):
    	if tstart<= xintercept15[i] <= tstop:
    		listaintersceptsx.append(xintercept15[i])
    		listaintersceptsy.append(yintercept15[i])



    plt.figure()
    plt.plot(x4, y4, c='r')
    plt.plot(x8, y8, c='g')
    plt.plot(x10, y10, c='b')
    plt.plot(x12, y12, c='yellow')
    plt.plot(x14, y14, c='purple')
    plt.plot(x16, y16, c='c')
    plt.plot(listaintersceptsx, listaintersceptsy, '*k')
    plt.xlabel('T')
    plt.ylabel('Binderov kumulant')
    plt.savefig("presek_kumulanata_SC.eps",dpi=300)
    plt.show()


    for i in range(0,len(listaintersceptsx)):
		print(listaintersceptsx[i])

    textfile = open("kumulanti_SC_preseci_pojedinacni.txt", "w")

    for element in listaintersceptsx:
        textfile.write(str(element) + "\n")
    textfile.close()