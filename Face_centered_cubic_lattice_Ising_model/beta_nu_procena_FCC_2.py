import numpy as np
import similaritymeasures
import matplotlib.pyplot as plt

pcm_lista=np.array([])
cl_lista=np.array([])

lista_beta=np.linspace(0.4,0.6,2001)

for beta_over_nu in np.linspace(0.4,0.6,2001):
	file=open('mag_rounded_t_redosled_3D_Ising_BCC.txt')

	file_data=np.loadtxt(file,usecols=(0,1))

	x=file_data[:,0]
	y=file_data[:,1]


	llista = [4,6,8,10,12,14,16] #lattice velicina
	n=21 #koraci

	for i in range(0,len(llista)):
		exec("x%d = x[i*n:i*n+n]" % (llista[i]));

	for j in range(0,len(llista)):
		exec("y%d = y[j*n:j*n+n]" % (llista[j]));

	tc=6.355 #procena
	a=1.59

	x10= ((x10-tc)/tc)*pow(float(10),a)
	x6= ((x6-tc)/tc)*pow(float(6),a)
	y10 = y10 / pow(float(10),-beta_over_nu)
	y6 = y6 / pow(float(6),-beta_over_nu)  

	
	g=np.where(np.logical_and(x10>=x6[np.argmin(x6)], x10<=x6[np.argmax(x6)]))


	x10novo = np.array([])
	y10novo = np.array([])

	for j in g[0]:
		x10novo=np.append(x10novo,x10[j])
		y10novo=np.append(y10novo,y10[j])
	

	data1 = np.zeros((n, 2))
	data1[:, 0] = x6
	data1[:, 1] = y6

	data2 = np.zeros((len(x10novo), 2))
	data2[:, 0] = x10novo
	data2[:, 1] = y10novo

	#PCM metod
	pcm = similaritymeasures.pcm(data1, data2)
	# CL metod
	cl = similaritymeasures.curve_length_measure(data1, data2)

	pcm_lista=np.append(pcm_lista,pcm)

	cl_lista=np.append(cl_lista,cl)
	
print(lista_beta[np.argmin(pcm_lista)])
print(lista_beta[np.argmin(cl_lista)])
