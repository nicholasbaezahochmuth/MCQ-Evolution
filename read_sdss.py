
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
from scipy import interpolate

cat = fits.getdata('//Python/sdss_compact_dr12_sn8_oii.fits', 1)
cat_file = cat['file']
cat_z = cat['z']

def read_sdss(name, z=0.):
    
    root = '//Python/Harvard/cg_data/spectra'
    file_name = root + '/' + name
    global image_data, title
    title = name
    image_data = fits.getdata(file_name, 1)
    image_data.lam = 10 ** image_data.loglam
    image_data.lam = image_data.lam / (z + 1)
    image_data.sigma = (1 / image_data.ivar) ** (.5)
