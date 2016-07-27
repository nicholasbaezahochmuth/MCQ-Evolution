import pylab as plb
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import asarray as ar,exp
from math import sqrt
from astropy.io import *
from astropy.io import fits
from matplotlib.pyplot import *
from scipy.special import wofz
ln2 = numpy.log(2)
import numpy
import pdb


""" 
    gaussindex() function for initial investigation in the data, to look at the plots and check the gaussian fits
"""

def gaussindex(image_data, lower_limit, upper_limit):
    index = numpy.where((image_data.lam > lower_limit) & (image_data.lam < upper_limit))
    x = image_data.lam[index]
    y = image_data.flux[index]
    n = len(x)                          #the number of data
    mean = sum(x)/n                   #note this correction
    #sigma = sqrt(sum(y*(x-mean)**2)/n) 
    #global popt, perr
    popt, pcov = curve_fit(gaus,x,y,p0=[1,mean,1,0], sigma = image_data.sigma[index])
    perr = numpy.sqrt(numpy.diag(pcov))
    plt.plot(x,y,label='data')
    plt.plot(x,gaus(x,*popt),label='fit',color='red')
    plt.title(title)
    plt.xlabel('Wavelength (angstroms)')
    plt.ylabel('Flux')
    #plt.savefig('//Users/nicholashochmuth/Python/Harvard/compact_galaxies/cg_output/Cont_test' + title + '.png')
    #plt.close()
    print popt, perr
    return popt
    return perr
    
    
