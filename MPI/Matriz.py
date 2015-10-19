'''
Created on 07/10/2015
@author: 		Leal
@version: 		3.4
'''

import numpy as np, random, time
from mpi4py import MPI


# MPI Init
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
p = comm.Get_size()

# Files
results = 'results.txt'
times = 'times.txt'
dim = 'dimensions.txt'

# Init Matrices
mat1 = np.load("../random-matrix-a.npy")
mat2 = np.load("../random-matrix-b.npy")

# Matrix Size
N = len(mat1)

# mat_result = np.zeros((N,N))

# Multiply Matrices
# mat_result = np.dot(mat1, mat2)
m = mat1.shape[0]/p

n = mat2.shape[0]/p


y_part = np.dot(mat1[rank * m:(rank+1)*m], mat2)
y = np.zeros_like(mat1)
comm.Allgather([y_part, MPI.DOUBLE], [y, MPI.DOUBLE])


# Save results in a file
if rank == 0:
	f = open(results,'a')
	for i in range(0, N):
		for j in range(0, N):
			f.write(' [%d] \n' % y[i][j])
	f.write('--------------------------------------------------------------\n')
	f.close()

	# Save the matrix size in the filesize
	fsize = open(dim, 'a')
	fsize.write('%d\n' % N)
	fsize.close()

	# Save the execution time second(s) in a filetime
	ftime = open(times, 'a')
	ftime.write('%f\n' % time.clock())
	ftime.close()
