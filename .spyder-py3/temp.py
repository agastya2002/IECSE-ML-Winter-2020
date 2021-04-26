import numpy as np
import seaborn as sns
import pandas as pd
from pandas_profiling import profile_report
.import sklearn
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
df = pd.read_csv("/Users/ashutosh/Desktop/diabetes.csv",delimiter=",")
X1 = df.iloc[:,:-1]
Y = df.iloc[:,-1]
X = preprocessing.scale(X1)
X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.3,random_state=42)
k_range = range(1,26)
scores = []
for k in range(1,26):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train,Y_train)
    Y_pred = knn.predict(X_test)
    scores.append(metrics.accuracy_score(Y_test,Y_pred))
    
    
plt.plot(k_range,scores)
for i in range(1,26):
    if scores[i-1]==max(scores):
        ind=i

print(ind)

knn = KNeighborsClassifier(n_neighbors=21)
knn.fit(X_train,Y_train)
Y_pred1 = knn.predict(X_test)
print(metrics.accuracy_score(Y_test,Y_pred1))


lg = LogisticRegression()
lg.fit(X_train,Y_train)
Y_pred2 = lg.predict(X_test)
print(metrics.accuracy_score(Y_test,Y_pred2))

svclassifier = SVC(kernel='linear')
svclassifier.fit(X_train, Y_train)
Y_pred3 = svclassifier.predict(X_test)
print(metrics.accuracy_score(Y_test,Y_pred3))












   













