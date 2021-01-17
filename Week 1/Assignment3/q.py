import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("python\IECSE-ML-Winter-2020\Week 1\Sample1.csv", names=['A','B'])

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Epic Info")
plt.plot(df['A'],df['B'])
plt.grid()
plt.show()