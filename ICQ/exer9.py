
import math
import cmath


x=2-1j
y=1+1j
print(f'A representacao polar de x sera: {abs(x):.2f} cis({math.degrees(cmath.phase(x)):.2f}°)')
print(f'A representacao polar de y sera: {abs(y):.2f} cis({math.degrees(cmath.phase(y)):.2f}°)')    
print(f'A representacao polar de x+y sera: {abs(y+x):.2f} cis({math.degrees(cmath.phase(y+x)):.2f}°)') 
print(f'A representacao polar de x-y sera: {abs(x-y):.2f} cis({math.degrees(cmath.phase(x-y)):.2f}°)') 
