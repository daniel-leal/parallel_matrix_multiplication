'''
Created on 07/10/2015
@author: 		Leal
@version: 		3.4
'''

import numpy as np, random, time

# Files
results = 'results.txt'
times = 'times.txt'
dim = 'dimensions.txt'

if __name__ == '__main__':

	# Init Matrices
	mat1 = np.load("../random-matrix-a.npy")
	mat2 = np.load("../random-matrix-b.npy")

	# Matrix Size
	N = len(mat1)

	mat_result = np.zeros((N,N))

	# Multiply Matrices
	mat_result = np.dot(mat1, mat2)

	# Save results in a file
	f = open(results,'a')
	for i in range(0, N):
		for j in range(0, N):
			f.write(' [%d] \n' % mat_result[i][j])
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
