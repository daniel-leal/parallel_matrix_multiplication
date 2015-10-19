import numpy as np

# Matrix Size
N = 5000

A = np.random.rand(N, N)
np.save("random-matrix-a.npy", A)

B = np.random.rand(N, N)
np.save("random-matrix-b.npy", A)
