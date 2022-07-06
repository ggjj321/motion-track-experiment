import numpy as np
import matplotlib.pyplot as plt

# fig = plt.figure()
# ax = fig.gca(projection='3d')

f = open('landmark.txt')
k = f.readlines()
x = []
y = []
for data in k:
    data_list = data.split()
    x.append(float(data_list[0]))
    y.append(float(data_list[1]))
z = list(range(1, len(x) + 1))
plt.title("track chart")

#ax.scatter(x, y, z, c=z, cmap='Reds', marker='^', label='My Points 1')
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.scatter(x, y)
plt.show()
f.close()