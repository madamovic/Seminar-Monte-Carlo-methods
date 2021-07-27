import numpy as np
import similaritymeasures
import matplotlib.pyplot as plt

pcm_lista=np.array([])
cl_lista=np.array([])

lista_a=np.linspace(0.8,1.1,3001)

for a in np.linspace(0.8,1.1,3001):
	file=open('binderdata_rounded_t_redosled_2D_Ising_Kagome.txt')

	file_data=np.loadtxt(file,usecols=(0,1))

	x=file_data[:,0]
	y=file_data[:,1]


	llista = [8,16,20,24,28,32,40] #lattice velicina
	n=41 #koraci

	for i in range(0,len(llista)):
		exec("x%d = x[i*n:i*n+n]" % (llista[i]));

	for j in range(0,len(llista)):
		exec("y%d = y[j*n:j*n+n]" % (llista[j]));

	tc=2.105 #procena

	x20= ((x20-tc)/tc)*pow(float(20),a)
	x40= ((x40-tc)/tc)*pow(float(40),a)
	
	g=np.where(np.logical_and(x40>=x20[np.argmin(x20)], x40<=x20[np.argmax(x20)]))


	x40novo = np.array([])
	y40novo=np.array([])

	for j in g[0]:
		x40novo=np.append(x40novo,x40[j])
		y40novo=np.append(y40novo,y40[j])
	

	data1 = np.zeros((n, 2))
	data1[:, 0] = x20
	data1[:, 1] = y20

	data2 = np.zeros((len(x40novo), 2))
	data2[:, 0] = x40novo
	data2[:, 1] = y40novo

	#PCM metod
	pcm = similaritymeasures.pcm(data1, data2)
	# CL metod
	cl = similaritymeasures.curve_length_measure(data1, data2)

	pcm_lista=np.append(pcm_lista,pcm)

	cl_lista=np.append(cl_lista,cl)
	
print(lista_a[np.argmin(pcm_lista)])
print(lista_a[np.argmin(cl_lista)])
