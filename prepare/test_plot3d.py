import matplotlib.pyplot as plt, numpy as np
from mpl_toolkits.mplot3d import Axes3D

v= np.array([[1,2,3], [4,5,6], [7,8,9]])
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(v[:,0],v[:,1],v[:,2])
plt.show()
