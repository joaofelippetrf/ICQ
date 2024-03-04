def delta(a,b,c):
    return b**2-4*a*c
def baskaraQuadratica(b,delta):
    return pow((-b+pow(delta,1/2))/2,1/2),pow((-b-pow(delta,1/2))/2,1/2)
    

res=delta(1,2,1)
x1,x2=baskaraQuadratica(2,res) # existem outras raizes -x1 -x2 nao mostradas
print(f'{x1} {x2}')

if isinstance(x1,complex) and isinstance(x2,complex):
    print('Nao ha solução real')
else :
    print('Existe solução real')