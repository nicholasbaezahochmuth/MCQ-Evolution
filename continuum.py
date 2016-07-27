import numpy as np

## simple continuum() function to concatenate the two flat sections of the spectra on either side of the 
## H-delta absorption line

def continuum(lam, flux):    
    index1 = np.where((lam > 4046) & (lam < 4076))
    index2 = np.where((lam > 4130) & (lam < 4150))
    [index1].extend([index2])
    global cont
    cont = numpy.median(flux[index1])
    
