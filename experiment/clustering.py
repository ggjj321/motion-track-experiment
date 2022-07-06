import numpy as np
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

f = open('landmark.txt')
k = f.readlines()
x = []
for data in k:
    data_list = data.split()
    x.append([float(data_list[0]), float(data_list[1])])

x = np.array(x)

# kmeans = KMeans(n_clusters=4, random_state=0).fit(x)
#
# print(kmeans.labels_)
#
# print(kmeans.cluster_centers_)
#
# plt.plot(kmeans.labels_)

clustering = DBSCAN(eps=0.035, min_samples=2)

clustering.fit(x)

labels = np.unique(clustering.labels_)

print(labels)

plt.plot(clustering.labels_)
plt.show()

