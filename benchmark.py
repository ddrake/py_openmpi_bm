from mpi4py import MPI
from datetime import datetime
import pickle

def read(name,directory=None):
    filename = name + '.pickle'
    path = filename if directory is None else directory + '/' + filename

indir = '/scratch/ddrake/'

i=0
a = read("a_{}".format(i),indir)

# MPI Initialization
main_id = 0
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

p = 23
iters=50
if rank == main_id:
    print("i={}, p=23, iters=50".format(i))
    print("started at \t{}".format(datetime.now().strftime("%H:%M:%S")))

# Main algorithm
for i in range(iters):
    if rank == main_id: # I'm the main process
        # I'll send a message to each of the helpers with u and v.
        for j in range(p):
            data = {'a': a}
            comm.send(data, dest=j+1, tag=11)
        for j in range(p):
            data = comm.recv(tag=12, source=j+1)
            b = data['b']
    else: # I am one of the helpers
        j = rank-1
        data = comm.recv(tag=11, source=main_id)
        b = data['a']
        data = {'b': b}
        comm.send(data, dest=main_id, tag=12)

if rank == main_id:
    print("finished at \t{}".format(datetime.now().strftime("%H:%M:%S")))

