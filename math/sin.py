import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-np.pi,np.pi,50)
y=np.sin(x)
plt.figure()
ax=plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))
plt.xlim(-4,4)
plt.ylim(-1.2,1.2)
plt.plot(x,y)
plt.show()
