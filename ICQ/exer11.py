import matplotlib.pyplot as plt
import numpy as np
x=complex(input('Digite um numero complexo : '))
r=np.linspace(0,5,50)
i=np.linspace(0,5,50)
real=np.zeros_like(r)
imag=np.zeros_like(r)
real=r*x.real
imag=r*x.imag
plt.figure()
plt.plot(real,imag,color='red',label='Numero complexo multiplicado por ro')
plt.plot(-imag,real,color='green',label='Numero complexo multiplicado por io')
plt.plot(x.real, x.imag,'ro', color='black',label='Numero complexo incial') 
plt.xlim(-5*x.real,5*x.real )
plt.ylim(-5*x.imag, 5*x.imag)
plt.xlabel('Parte real')
plt.ylabel('Parte imaginaria')
plt.legend()
plt.grid()
plt.show()



