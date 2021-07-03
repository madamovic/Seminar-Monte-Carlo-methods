import numpy as np
import similaritymeasures
import matplotlib.pyplot as plt

pcm_lista=np.array([])
cl_lista=np.array([])

lista_eta=np.linspace(0.0,3.0,3001)

for two_minus_eta in np.linspace(0.0,3.0,3001):
	file=open('susc_rounded_t_redosled_2D_Ising_triangular.txt')

	file_data=np.loadtxt(file,usecols=(0,1))

	x=file_data[:,0]
	y=file_data[:,1]


	llista = [8,16,24,32,40] #lattice velicina
	n=61 #koraci

	for i in range(0,len(llista)):
		exec("x%d = x[i*n:i*n+n]" % (llista[i]));

	for j in range(0,len(llista)):
		exec("y%d = y[j*n:j*n+n]" % (llista[j]));

	tc=3.622 #procena
	a=0.992

	x16= ((x16-tc)/tc)*pow(float(16),a)
	x24= ((x24-tc)/tc)*pow(float(24),a)
	y16 = y16 / pow(float(16),two_minus_eta)
	y24 = y24 / pow(float(24),two_minus_eta)  

	
	g=np.where(np.logical_and(x24>=x16[np.argmin(x16)], x24<=x16[np.argmax(x16)]))


	x24novo = np.array([])
	y24novo=np.array([])

	for j in g[0]:
		x24novo=np.append(x24novo,x24[j])
		y24novo=np.append(y24novo,y24[j])
	

	data1 = np.zeros((n, 2))
	data1[:, 0] = x16
	data1[:, 1] = y16

	data2 = np.zeros((len(x24novo), 2))
	data2[:, 0] = x24novo
	data2[:, 1] = y24novo

	#PCM metod
	pcm = similaritymeasures.pcm(data1, data2)
	# CL metod
	cl = similaritymeasures.curve_length_measure(data1, data2)

	pcm_lista=np.append(pcm_lista,pcm)

	cl_lista=np.append(cl_lista,cl)
	
print(lista_eta[np.argmin(pcm_lista)])
print(lista_eta[np.argmin(cl_lista)])
