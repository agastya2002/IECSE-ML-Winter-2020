import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv('Week-1\Sample.csv', names=['A','B'])


plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Epic Info")
plt.plot(df['A'],df['B'])
plt.grid()
plt.show()