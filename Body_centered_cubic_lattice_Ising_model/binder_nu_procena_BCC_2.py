import numpy as np
import similaritymeasures
import matplotlib.pyplot as plt

pcm_lista=np.array([])
cl_lista=np.array([])

lista_a=np.linspace(1.5,2.0,501)

for a in np.linspace(1.5,2.0,501):
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

	tc=6.355 #procena

	x10= ((x10-tc)/tc)*pow(float(10),a)
	x12= ((x12-tc)/tc)*pow(float(12),a)
	
	g=np.where(np.logical_and(x12>=x10[np.argmin(x10)], x12<=x10[np.argmax(x10)]))


	x12novo = np.array([])
	y12novo=np.array([])

	for j in g[0]:
		x12novo=np.append(x12novo,x12[j])
		y12novo=np.append(y12novo,y12[j])
	

	data1 = np.zeros((n, 2))
	data1[:, 0] = x10
	data1[:, 1] = y10

	data2 = np.zeros((len(x12novo), 2))
	data2[:, 0] = x12novo
	data2[:, 1] = y12novo



	#PCM metod
	pcm = similaritymeasures.pcm(data1, data2)
	# CL metod
	cl = similaritymeasures.curve_length_measure(data1, data2)

	pcm_lista=np.append(pcm_lista,pcm)

	cl_lista=np.append(cl_lista,cl)
	
print(lista_a[np.argmin(pcm_lista)])
print(lista_a[np.argmin(cl_lista)])
