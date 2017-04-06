import pandas as pd
import numpy as np
import time
from sklearn.cross_validation import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
start = time.clock()

# 读取训练数据
dataSet = pd.read_csv("train.csv")
trainData = dataSet.values[0:, 1:]
label = dataSet.values[0:, 0]

# 切分数据用于快速迭代
trainDataSmall = trainData[:10000, :]
labelSmall = label[:10000]

# 读取测试数据
testDataSet = pd.read_csv("test.csv").values

knn_clf = KNeighborsClassifier(n_neighbors = 5, algorithm = 'kd_tree', weights='distance', p=3)
score = cross_val_score(knn_clf, trainDataSmall, labelSmall, cv = 3)
print(score.mean())
#end time
elapsed = (time.clock() - start)
print("Time used:",int(elapsed), "s")

clf=knn_clf

start = time.clock()
clf.fit(trainData,label)
elapsed = (time.clock() - start)
print("Training Time used:",int(elapsed/60) , "min")

result=clf.predict(testDataSet)
result = np.c_[range(1,len(result)+1), result.astype(int)]
df_result = pd.DataFrame(result, columns=['ImageId', 'Label'])

df_result.to_csv('knn.csv', index=False)
#end time
elapsed = (time.clock() - start)
print("Test Time used:",int(elapsed/60) , "min")