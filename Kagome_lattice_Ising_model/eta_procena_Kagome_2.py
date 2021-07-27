import numpy as np
import similaritymeasures
import matplotlib.pyplot as plt

pcm_lista=np.array([])
cl_lista=np.array([])

lista_eta=np.linspace(1.2,2.0,2001)

for two_minus_eta in np.linspace(1.2,2.0,2001):
	file=open('susc_rounded_t_redosled_2D_Ising_Kagome.txt')

	file_data=np.loadtxt(file,usecols=(0,1))

	x=file_data[:,0]
	y=file_data[:,1]


	llista = [8,16,24,32,40] #lattice velicina
	n=41 #koraci

	for i in range(0,len(llista)):
		exec("x%d = x[i*n:i*n+n]" % (llista[i]));

	for j in range(0,len(llista)):
		exec("y%d = y[j*n:j*n+n]" % (llista[j]));

	tc=2.105 #procena
	a=1.0509

	x16= ((x16-tc)/tc)*pow(float(16),a)
	x8= ((x8-tc)/tc)*pow(float(8),a)
	y16 = y16 / pow(float(16),two_minus_eta)
	y8 = y8 / pow(float(8),two_minus_eta)  

	
	g=np.where(np.logical_and(x16>=x8[np.argmin(x8)], x16<=x8[np.argmax(x8)]))


	x16novo = np.array([])
	y16novo=np.array([])

	for j in g[0]:
		x16novo=np.append(x16novo,x16[j])
		y16novo=np.append(y16novo,y16[j])
	

	data1 = np.zeros((n, 2))
	data1[:, 0] = x8
	data1[:, 1] = y8

	data2 = np.zeros((len(x16novo), 2))
	data2[:, 0] = x16novo
	data2[:, 1] = y16novo

	#PCM metod
	pcm = similaritymeasures.pcm(data1, data2)
	# CL metod
	cl = similaritymeasures.curve_length_measure(data1, data2)

	pcm_lista=np.append(pcm_lista,pcm)

	cl_lista=np.append(cl_lista,cl)
	
print(lista_eta[np.argmin(pcm_lista)])
print(lista_eta[np.argmin(cl_lista)])
