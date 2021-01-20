import matplotlib.pyplot as plt
import pandas as pd 

df=pd.read_csv("C:\\Users\Manvendra\IECSE-ML-Winter-2020\Week 1\Assignment-3 (Using Matplotlib)\data.csv",names=['x','y'])
plt.figure()
plt.style.use('ggplot')
plt.plot(df['x'],df['y'],'-r')
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.suptitle("Epic Info")
plt.show()
