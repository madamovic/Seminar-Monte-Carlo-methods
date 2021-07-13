import numpy as np
import similaritymeasures
import matplotlib.pyplot as plt

pcm_lista=np.array([])
cl_lista=np.array([])

lista_eta=np.linspace(0.0,3.0,3001)

for two_minus_eta in np.linspace(0.0,3.0,3001):
	file=open('susc_rounded_t_redosled_3D_Ising_SC.txt')

	file_data=np.loadtxt(file,usecols=(0,1))

	x=file_data[:,0]
	y=file_data[:,1]


	llista = [4,6,8,10,12,14,16] #lattice velicina
	n=41 #koraci

	for i in range(0,len(llista)):
		exec("x%d = x[i*n:i*n+n]" % (llista[i]));

	for j in range(0,len(llista)):
		exec("y%d = y[j*n:j*n+n]" % (llista[j]));

	tc=4.52 #procena
	a=1.519

	x8= ((x8-tc)/tc)*pow(float(8),a)
	x10= ((x10-tc)/tc)*pow(float(10),a)
	y8 = y8 / pow(float(8),two_minus_eta)
	y10 = y10 / pow(float(10),two_minus_eta)  

	
	g=np.where(np.logical_and(x10>=x8[np.argmin(x8)], x10<=x8[np.argmax(x8)]))


	x10novo = np.array([])
	y10novo=np.array([])

	for j in g[0]:
		x10novo=np.append(x10novo,x10[j])
		y10novo=np.append(y10novo,y10[j])
	

	data1 = np.zeros((n, 2))
	data1[:, 0] = x8
	data1[:, 1] = y8

	data2 = np.zeros((len(x10novo), 2))
	data2[:, 0] = x10novo
	data2[:, 1] = y10novo

	#PCM metod
	pcm = similaritymeasures.pcm(data1, data2)
	# CL metod
	cl = similaritymeasures.curve_length_measure(data1, data2)

	pcm_lista=np.append(pcm_lista,pcm)

	cl_lista=np.append(cl_lista,cl)
	
print(lista_eta[np.argmin(pcm_lista)])
print(lista_eta[np.argmin(cl_lista)])
