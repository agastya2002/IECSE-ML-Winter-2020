import numpy as np
import matplotlib.pyplot as pl
x= np.arange(1,16,1)
print(x)
y= [5,7,8,3,5,6,3,7,2,12,5,7,2,6,9,2]
pl.xlabel("X axis")
pl.ylabel("Y axis")
pl.title("Epic info")
pl.plot(x,y)
pl.show()
