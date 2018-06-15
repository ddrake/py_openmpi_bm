from numpy import *
import pickle

def save(obj, name, directory=None):
    path = name if directory is None else directory + '/' + name
    with open('{}.pickle'.format(path),'wb') as f:
        pickle.dump(obj, f)


outdir = '/scratch/ddrake/'
for i in range(7):
    a = random.rand(10**i)
    save(a,"a_{}".format(i),outdir)


