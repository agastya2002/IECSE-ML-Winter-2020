import matplotlib.pyplot as plt
import pandas as pd

data_frame = pd.read_csv("D:\VS Code\IECSE-ML-Winter-2020\Week-1\Sample.csv", names =["A","B"])
print(data_frame)
plt.suptitle("Epic Info")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid()
plt.plot(data_frame["A"],data_frame["B"], color = "Red")
plt.show()
#file_data = open("D:\VS Code\IECSE-ML-Winter-2020\Week-1\Sample.csv","r")
#list_of_lines = file_data.readlines()
#x_axis = []
#y_axis = []
#ax = plt.axes()
#for line in list_of_lines:
    #temp_list = line.split(",")
    #x_axis.append(temp_list[0])
    #y_axis.append(temp_list[1])

#ax.set_xticks([2,4,6,8,10,12,14,16])
#ax.set_yticks([2,4,6,8,10,12])
#ax.plot(x_axis,y_axis,color = "red")
#plt.show()

