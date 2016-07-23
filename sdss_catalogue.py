import warnings

def sdss_catalogue(size_array):
    global cat_values    
    cat_values = []
    for i in range(0,size_array):
        read_sdss(cat_file[i], cat_z[i])
        fitsdss_hdelta(image_data.lam, image_data.flux, image_data.sigma)   
        cat_values.append(val)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=RuntimeWarning)
