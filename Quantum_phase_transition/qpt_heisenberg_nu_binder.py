from scipy import interpolate
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def derivative(f,a,method='central',h=0.001):
    if method == 'central':
        return (f(a + h) - f(a - h))/(2*h)
    elif method == 'forward':
        return (f(a + h) - f(a))/h
    elif method == 'backward':
        return (f(a) - f(a - h))/h
    else:
        raise ValueError("Method must be 'central', 'forward' or 'backward'.")


file=open('binderdata_rounded_heisenberg_redosled.txt')

file_data=np.loadtxt(file,usecols=(0,1))

x=file_data[:,0]
y=file_data[:,1]
llista = [8,10,12,16]
n=101

for i in range(0,len(llista)):
    exec("x%d = x[i*n:i*n+n]" % (llista[i]));

for j in range(0,len(llista)):
    exec("y%d = y[j*n:j*n+n]" % (llista[j]));

#funk = interpolate.interp1d(x, y)

for k in range(0,len(llista)):
    exec("funk%d = interpolate.interp1d(x%d, y%d, fill_value='extrapolate' )" % (llista[k],llista[k],llista[k]));

for l in range(0,len(llista)):
    exec("xizv%d = np.arange(0.1,0.6,0.001)" % (llista[l]));

for m in range(0,len(llista)):
    exec("yizv%d = derivative(funk%d,xizv%d)" % (llista[m],llista[m],llista[m]));
    

lista=[]
jc=0.32

for p in range(0,len(llista)):
    exec("rez = derivative(funk%d,jc)" % (llista[p]));
    lista.append(rez)

plt.figure()
plt.plot(x12,y12,label='$U_{4}$',color='b')
plt.plot(xizv12,yizv12,label='$dU_{4}/dT$',color='r')
plt.legend(loc='best')
plt.savefig("figure_derivative_binder_1.eps",dpi=300)


from scipy import optimize

def test_funk(x,a,b):
    return a*x**b

params,params_covariance=optimize.curve_fit(test_funk,llista,lista)

print(params[0],params[1])
print(np.sqrt(np.diag(params_covariance)))

plt.figure()
plt.scatter(llista,lista,label='Podaci',color='b')
plt.plot(llista,test_funk(llista,params[0],params[1]),label='Fit',color='r')
plt.xlabel('$L$')
plt.ylabel(r'$dU_{4}/dJ_{2}|J_{2}^{C}\approx L^{1/\nu}$')
plt.title(r'$1/\nu=$ %.13s,$\nu=$ %.13s' % (params[1],1/params[1]))
plt.legend(loc='upper left')
plt.savefig("figure_derivative_binder_2.eps",dpi=300)






