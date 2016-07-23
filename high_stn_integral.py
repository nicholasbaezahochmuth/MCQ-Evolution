"""High STN Integration"""

import numpy as np

def high_stn_integral(n, lower_limit=4076., upper_limit=4130.):
    read_sdss(cat_file[n], cat_z[n])
    areaindex = np.where((image_data.lam > lower_limit) & (image_data.lam < upper_limit))
    continuum(image_data.lam, image_data.flux)    
    flux = (image_data.flux / cont) - 1
    sigma = (image_data.sigma / cont)
    plt.plot(image_data.lam[areaindex], flux[areaindex])
    area = np.absolute(np.sum(flux[areaindex]))
    area_error = np.sqrt(np.sum((sigma ** 2)[areaindex]))
    print 'Integral Area:',  area
    print 'Integral Area Error:',  area_error
    
    
    
def high_stn_integral2(n):
    global area2, area_error2
    read_sdss(cat_file[n], cat_z[n])
    fitsdss_hdelta2(image_data.lam, image_data.flux, image_data.sigma)
    dx = (np.max(x1) - np.min(x1)) / (len(x1)-1)
    area2 = np.absolute(np.sum(y2 * dx))
    area_error2 = np.sqrt(np.sum(sigma2 ** 2))
    print 'Integral Area:', area2
    print 'Integral Area Error:', area_error2

def area_diff_list(n):
    area_diff_list2 = []    
    for i in range(0,n):
        high_stn_integral2(highstn_index[0][i])
        area_diff = area - area2
        area_error_diff = area_error - area_error2
        area_diff_list2.append(area_diff)
    print area_diff_list2