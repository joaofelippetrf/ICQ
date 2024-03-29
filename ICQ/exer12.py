import matplotlib.pyplot as plt
import cmath
def operador(z,n) :
    r =z
    while n>1 :
        r *=z
        n-=1
    return r

z=complex(input('Digite um numero complexo: '))
pontos_real = []
pontos_imaginarios = []
for n in range(1, 11):
    resultado = operador(z, n)
    pontos_real.append(resultado.real)
    pontos_imaginarios.append(resultado.imag)

plt.figure(figsize=(8, 6))
plt.plot(pontos_real, pontos_imaginarios, 'bo-', label='z^n')
plt.plot([0], [0], 'ro', label='Origem (0, 0)')
plt.xlim(-abs(operador(z,10)),abs(operador(z,10)))

plt.xlabel('Parte Real')
plt.ylabel('Parte Imaginária')
plt.title(f'Potências de {z}')
plt.legend()
plt.grid()
plt.show()