c1=eval(input(' Digite um numero: '))
c2=eval(input(' Digite um numero: '))

def mod(x):
    return pow(x.real*x.real +x.imag*x.imag,1/2)

if mod(c1*c2)==mod(c1)*mod(c2):
    print(f'Os 2 lados da expressao valem {mod(c1*c2)}')
if mod(c1+c2)<=mod(c1)+mod(c2):
    print(f'O lado esquerdo e menor ou igual e vale {mod(c1+c2)}e o lado direito vale {mod(c1)+mod(c2)}')