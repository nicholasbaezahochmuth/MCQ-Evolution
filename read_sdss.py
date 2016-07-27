
#http://stackoverflow.com/questions/19206332/gaussian-fit-for-python

##     Import of all of the packages used in this project, for reference at least

import pylab as plb
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import asarray as ar,exp
from math import sqrt
from astropy.io import *
from astropy.io import fits
from matplotlib.pyplot import *
import numpy
from scipy import interpolate

##       using SDSS MCQ catalogue FITS file to create "cat" data table
##       isolate the cat_file (file name) and cat_z (redshift) data to use
##       in the read_sdss() function

cat = fits.getdata('~/sdss_compact_dr12_sn8_oii.fits', 1)
cat_file = cat['file']
cat_z = cat['z']

##      read_sdss() function to read in galaxy spectra file and return corrected wavelength and standard deviation
##          input: filename, redshift
##          output: image_data.lam (wavelength corrected for redshift and originally log format)
##                  image_data.sigma (inverse variance converted to standard deviation)

def read_sdss(name, z=0.):
    
    root = '~/spectra'
    file_name = root + '/' + name
    global image_data, title
    title = name
    image_data = fits.getdata(file_name, 1)
    image_data.lam = 10 ** image_data.loglam
    image_data.lam = image_data.lam / (z + 1)
    image_data.sigma = (1 / image_data.ivar) ** (.5)
