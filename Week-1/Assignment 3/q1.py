import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("Sample.csv", names=['A','B'])

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("Epic Info")
plt.plot(df['A'],df['B'])
plt.grid()
plt.show()

