import matplotlib.pyplot as plt

x = [2,-1]  
y=[1,1]

plt.figure(num='Soma de vetores')
plt.quiver(0, 0,x[0],x[1],angles='xy',scale_units='xy',scale=1,color='b',label='X')
plt.quiver(0,0,y[0],y[1],angles='xy',scale_units='xy',scale=1,color='r',label='Y')
plt.quiver(0,0,x[0]-y[0],x[1]-y[1],angles='xy',scale_units='xy',scale=1,color='g',label='subtracao')
plt.text(x[0]-y[0], -y[1]+x[1], 'x-y', fontsize=12,  verticalalignment='bottom', horizontalalignment='left')
plt.text(x[0], x[1], 'x', fontsize=12,  verticalalignment='bottom', horizontalalignment='right')
plt.text(y[0], y[1], 'y', fontsize=12,  verticalalignment='bottom', horizontalalignment='right')
plt.xlim(-0, 3)
plt.ylim(-3, 3)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.title('Vetores x e y')
plt.show()


plt.figure(num='Subtracao de vetores')
plt.quiver(0, 0,x[0],x[1],angles='xy',scale_units='xy',scale=1,color='b',label='X')
plt.quiver(0,0,y[0],y[1],angles='xy',scale_units='xy',scale=1,color='r',label='Y')
plt.quiver(0,0,x[0]+y[0],x[1]+y[1],angles='xy',scale_units='xy',scale=1,color='g',label='Soma')
plt.text(x[0]+y[0], +y[1]+x[1], 'x+y', fontsize=12,  verticalalignment='bottom', horizontalalignment='right')
plt.text(x[0], x[1], 'x', fontsize=12,  verticalalignment='bottom', horizontalalignment='right')
plt.text(y[0], y[1], 'y', fontsize=12,  verticalalignment='bottom', horizontalalignment='right')
plt.xlim(-0, 4)
plt.ylim(-3, 4)
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.title('Vetores x e y')
plt.show()

