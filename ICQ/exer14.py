def moebius(a,b,c,d,x):
    return (a*x+b)/(c*x+d)


x=1+1j

print(f'{moebius(0,1,1,0,x):.2f}')

