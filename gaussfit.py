#http://stackoverflow.com/questions/19206332/gaussian-fit-for-python

import pylab as plb
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import asarray as ar,exp
from math import sqrt
from astropy.io import *
from astropy.io import fits
from matplotlib.pyplot import *
import numpy


def gaussfit(data):
    x = data.lam
    y = data.flux
    n = len(x)                          #the number of data
    mean = sum(x)/n                   #note this correction
    #sigma = sqrt(sum(y*(x-mean)**2)/n) 
    global popt, perr
    popt, pcov = curve_fit(gaus,x,y,p0=[1,mean,1,0], sigma=image_data.sigma)
    perr = numpy.sqrt(numpy.diag(pcov))
    plt.plot(x,y,label='data')
    #plt.plot(x,gaus(x,*popt),label='fit',color='red')
    plt.xlabel('Wavelength (angstroms)')
    plt.ylabel('Flux')
    return perr
       #note this correction

def gaus(x,*p):
    a = p[0]
    x0 = p[1]
    sig = p[2]
    Cons = p[3]
    return a*exp(-(x-x0)**2/(2*sig**2))+Cons