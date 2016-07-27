"""High STN Integration"""

import numpy as np

    
"""
    high_stn_integral2() function is used to take the integral of the H-delta absorption line to find the area under the curve
    this value was compared to the area of the gaussian fit to test the accuracy of the method
    
    input:  n = file number (to call from SDSS spectra catalogue)
            lower and upper limit (to define H-delta aborption line location)
    output: area, area_error (to be compared to Gaussian values)
"""
    
def high_stn_integral2(n):
    global area2, area_error2
    read_sdss(cat_file[n], cat_z[n])
    fitsdss_hdelta2(image_data.lam, image_data.flux, image_data.sigma)
    dx = (np.max(x1) - np.min(x1)) / (len(x1)-1)
    area2 = np.absolute(np.sum(y2 * dx))
    area_error2 = np.sqrt(np.sum(sigma2 ** 2))
    print 'Integral Area:', area2
    print 'Integral Area Error:', area_error2

"""
    area_diff_list() function to create a list of the comparisons between the Gaussian fit area, and the Integral area
    used to calculate accuracy of the fit
"""

def area_diff_list(n):
    area_diff_list2 = []    
    for i in range(0,n):
        high_stn_integral2(highstn_index[0][i])
        area_diff = area - area2
        area_error_diff = area_error - area_error2
        area_diff_list2.append(area_diff)
    print area_diff_list2
