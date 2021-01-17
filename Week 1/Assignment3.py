import pandas as pd
import matplotlib.pyplot as plt

obj =pd.read_csv("Sample1.csv")
X = obj.iloc[:,0]
Y = obj.iloc[:,1]
plt.plot(X,Y,color = "red")
plt.grid()
plt.title("Epic Info")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.show()