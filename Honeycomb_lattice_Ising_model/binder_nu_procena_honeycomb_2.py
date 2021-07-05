import numpy as np
import similaritymeasures
import matplotlib.pyplot as plt

pcm_lista=np.array([])
cl_lista=np.array([])

lista_a=np.linspace(0.0,1.5,1501)

for a in np.linspace(0.0,1.5,1501):
	file=open('binderdata_rounded_t_redosled_2D_Ising_honeycomb.txt')

	file_data=np.loadtxt(file,usecols=(0,1))

	x=file_data[:,0]
	y=file_data[:,1]


	llista = [8,16,24,28,32,40] #lattice velicina
	n=41 #koraci

	for i in range(0,len(llista)):
		exec("x%d = x[i*n:i*n+n]" % (llista[i]));

	for j in range(0,len(llista)):
		exec("y%d = y[j*n:j*n+n]" % (llista[j]));

	tc=1.504 #procena

	x16= ((x16-tc)/tc)*pow(float(16),a)
	x28= ((x28-tc)/tc)*pow(float(28),a)
	
	g=np.where(np.logical_and(x28>=x16[np.argmin(x16)], x28<=x16[np.argmax(x16)]))


	x28novo = np.array([])
	y28novo=np.array([])

	for j in g[0]:
		x28novo=np.append(x28novo,x28[j])
		y28novo=np.append(y28novo,y28[j])
	

	data1 = np.zeros((n, 2))
	data1[:, 0] = x16
	data1[:, 1] = y16

	data2 = np.zeros((len(x28novo), 2))
	data2[:, 0] = x28novo
	data2[:, 1] = y28novo

	#PCM metod
	pcm = similaritymeasures.pcm(data1, data2)
	# CL metod
	cl = similaritymeasures.curve_length_measure(data1, data2)

	pcm_lista=np.append(pcm_lista,pcm)

	cl_lista=np.append(cl_lista,cl)
	
print(lista_a[np.argmin(pcm_lista)])
print(lista_a[np.argmin(cl_lista)])
