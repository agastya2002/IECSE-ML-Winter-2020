import matplotlib.pyplot as plt
import numpy as np
x= np.arange(1,17)
y= np.array([5,7,8,3,5,6,3,7,2,12,5,7,2,6,9,2])
plt.plot(x, y,'-')
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Epic Info")
plt.show()