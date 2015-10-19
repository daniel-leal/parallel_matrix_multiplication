'''
Created on 17/10/2015
@author:        Leal
@version:       3.4
'''

from pylab import *

class Graph():

    def __init__(self):

        # Init Seq data
        self.ftimes_seq = open('Sequential/times.txt').read().splitlines()
        self.fsizes_seq = open('Sequential/dimensions.txt').read().splitlines()

        # Init MPI Data
        self.ftimes_mpi = open('MPI/times.txt').read().splitlines()
        self.fsizes_mpi = open('MPI/dimensions.txt').read().splitlines()

        # Func Points
        self.x_seq = []
        self.y_seq = []
        self.x_mpi = []
        self.y_mpi = []

    def read_params(self):

        # Read Seq data
        for i in self.fsizes_seq:
            self.x_seq.append(i)
        for i in self.ftimes_seq:
            self.y_seq.append(i)

        # Read MPI data
        for i in self.fsizes_mpi:
            self.x_mpi.append(i)
        for i in self.ftimes_mpi:
            self.y_mpi.append(i)

    def show_graph(self):
        self.read_params()
        plot(self.x_seq, self.y_seq, 'bo:', self.x_mpi, self.y_mpi, 'g^-')
        xlabel('Dimension (NxN)')
        ylabel('Times (sec)')
        title('Sequential Execution Time')
        legend(['Sequencial', 'MPI'])
        grid(False)
        show()

    def run(self):
        self.show_graph()

g = Graph()
g.run()
