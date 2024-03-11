import matplotlib.pyplot as plt
import cmath
def operador(z,n) :
    r =z
    while n>0 :
        r += 1j
        n -=1
    return r


z=complex(input('Digite um numero complexo'))
pontos_real = []
pontos_imaginarios = []
for n in range(1, 11):
    resultado = operador(z, n)
    pontos_real.append(resultado.real)
    pontos_imaginarios.append(resultado.imag)

plt.figure(figsize=(8, 6))
plt.plot(pontos_real, pontos_imaginarios, 'bo-', label='z^n')
plt.plot([0], [0], 'ro', label='Origem (0, 0)')
plt.xlim(-z.real,z.real+5)
plt.ylim(-z.imag,z.imag+20)
plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')
plt.title(f'z+nj')
plt.legend()
plt.grid()
plt.show()