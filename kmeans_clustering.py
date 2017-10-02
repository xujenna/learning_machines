import numpy as np
import matplotlib.pyplot as plt


c = input("How many clusters? ")
c = int(c)

n = 100
x = np.random.rand(n,2)
v = np.random.rand(c,2)

plt.scatter(x[:,0], x[:,1], marker='.') # data set

plt.scatter(v[:,0], v[:,1], c='r') # clusters

plt.show()

while True:
	clusters = np.zeros(n)
	for i in range(n): # iterates n (size of data set) times
		ith_row = x[i] # access indices of data set
		distances = []
		for j in v:
			distances.append(np.linalg.norm(ith_row-j)) # calculates distance & appends
		clusters[i] = np.argmin(distances) # inserts smallest distance INDEX to array

	for j in range(c): # iteraates c (number of cluster centers) times
		new_cluster_center = np.zeros(2)
		k = 0
		for i in range(n): 
			if clusters[i] == j: # identifies data points that belong to cluster set j
				new_cluster_center += x[i] # vector addition of data points
				k += 1 # counter of cluster set
		new_cluster_center = new_cluster_center / k # takes the average of all data points
		v[j] = new_cluster_center # inserts new cluster center into cluster set v

	new_clusters = np.zeros(n)

	for i in range(n):
		ith_row = x[i]
		distances = []
		for j in v:
			distances.append(np.linalg.norm(ith_row-j))
		new_clusters[i] = np.argmin(distances)

	if np.array_equal(new_clusters, clusters):
		plt.scatter(x[:,0], x[:,1], marker='.')
		plt.scatter(v[:,0], v[:,1], c='black')
		plt.show()
		print(v)
		break
	else:
		plt.scatter(x[:,0], x[:,1], marker='.')
		plt.scatter(v[:,0], v[:,1], c='r')
		plt.show()
		print(v)





# for j in range(c):
# 	cj = indices_of_points_in_cluster_j
# 	plt.scatter(x[cj,0], x[cj,1], c=....)




