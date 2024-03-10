import math
import cmath
def conversao(a,b):
    x=complex(a,b)
    return abs(x),math.degrees(cmath.phase(x))
n=[0,0]
n[0]=float(input('Digite a parte real do numero complexo'))
n[1]=float(input('Digite a parte imaginaria do numero complexo'))
y=conversao(n[0],n[1])
print(f'({y[0]:.2f},{y[1]:.2f})')

