# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 10:57:07 2015

@author: nicholashochmuth
"""

"""
    fits_EAcatalogue() function used to create a FITS table from the data exported through the curve fitting process.
    There is definitely a more efficient way of doing this, but at this point I had not learned much about Pandas or 
    more efficient data manipulation
"""


def fits_EAcatalogue(c, f):
    #global size    
    size = len(f)
    #global a_list, x0_list, area_list
    filename_list = []
    a_list = []
    x0_list = []
    sig_list = []
    Cons_list = []
    a_error_list = []
    x0_error_list = []
    sig_error_list = []
    Cons_error_list = []
    area_list = []
    area_error_list = []
    for i in range(0,150):
        filename_list.append(c[f[0][i]][0])
        a_list.append(c[f[0][i]][1])
        x0_list.append(c[f[0][i]][2])
        sig_list.append(c[f[0][i]][3])        
        Cons_list.append(c[f[0][i]][4])
        a_error_list.append(c[f[0][i]][5])
        x0_error_list.append(c[f[0][i]][6])
        sig_error_list.append(c[f[0][i]][7])        
        Cons_error_list.append(c[f[0][i]][8])
        area_list.append(c[f[0][i]][9])
        area_error_list.append(c[f[0][i]][10])
    col0 = fits.Column(name='File', format='32a', array=filename_list)
    col1 = fits.Column(name='A', format='E', array=a_list)
    col2 = fits.Column(name='A Error', format='E', array=a_error_list)
    col3 = fits.Column(name = 'x0', format='E', array=x0_list)
    col4 = fits.Column(name='x0 Error', format='E', array=x0_error_list)
    col5 = fits.Column(name='Sigma', format='E', array=sig_list)
    col6 = fits.Column(name = 'Sigma Error', format='E', array=sig_error_list)
    col7 = fits.Column(name='Constant', format='E', array=Cons_list)
    col8 = fits.Column(name='Constant Error', format='E', array=Cons_error_list)
    col9 = fits.Column(name='Area', format='E', array=area_list)
    col10 = fits.Column(name='Area Error', format='E', array=area_error_list)
    cols = fits.ColDefs([col0, col1, col2, col3, col4, col5, col6, col7, col8, col9, col10])
    tbhdu = fits.BinTableHDU.from_columns(cols)
    tbhdu.writeto('~/EA_Catalog.fits')
