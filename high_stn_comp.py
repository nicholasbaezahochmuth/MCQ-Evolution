"""High STN Area Comparison"""

def high_stn_comp(i, data, lower_limit=4076., upper_limit=4130.):
    signaltonoise = data['Area'] / data['Area Error']
    highstn_index = np.where((data['Sigma'] > 5) & (signaltonoise > 10))
    read_sdss(cat_file[i], cat_z[i])
    continuum(image_data.lam, image_data.flux)
    index = numpy.where((image_data.lam > 4076) & (image_data.lam < 4130))
    x = image_data.lam[index]
    y = image_data.flux[index] / cont - 1
    n = len(x)                          #the number of data
    mean = sum(x)/n                   #note this correction
    popt, pcov = curve_fit(gaus,x,y,p0=[1,mean,1,0], sigma = (image_data.sigma[index] / cont))
    perr = numpy.sqrt(numpy.diag(pcov))
    plt.plot(x,y,label='data')
    plt.plot(x,gaus(x,*popt),label='fit',color='red')
    plt.xlabel('Wavelength (angstroms)')
    plt.ylabel('Flux')
    plt.title(cat_file[i])
    gaus_area = numpy.absolute(popt[0]*popt[2]*sqrt(2*numpy.pi)) ## double check "2*pi"
    gaus_area_error = gaus_area*(sqrt(((perr[0]/popt[0])**2)+((perr[2]/popt[2])**2)))
    print 'Gaussian Area:', gaus_area 
    print 'Gaussian Area Error:', gaus_area_error
    high_stn_integral(i, data, lower_limit, upper_limit)
