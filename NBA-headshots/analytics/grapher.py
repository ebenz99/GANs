import matplotlib.pyplot as plt 
import numpy as np



numgraphed = 30000

idx = 0
darr = np.ndarray(shape=(numgraphed), dtype = "float")
idxs = np.ndarray(shape=(numgraphed), dtype = "float")


with open("analytics.txt","r") as f:
	for line in f:
		first = line.split(",")[0]
		number = first.split(" ")[-1]
		darr[idx] = np.float(number)
		idxs[idx] = np.float(idx)
		idx += 1
		if idx >= numgraphed:
			break

fig = plt.figure()
ax = plt.axes()
ax.plot(idxs, darr);
plt.show()