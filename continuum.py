import numpy as np

def continuum(lam, flux):    
    index1 = np.where((lam > 4046) & (lam < 4076))
    index2 = np.where((lam > 4130) & (lam < 4150))
    [index1].extend([index2])
    global cont
    cont = numpy.median(flux[index1])
    