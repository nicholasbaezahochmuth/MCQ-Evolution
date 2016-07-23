"""High S/N Cutoff"""

def high_stn_cutoff(data):
    signaltonoise = data['Area'] / data['Area Error']
    highstn_index = np.where((data['Sigma'] > 5) & (signaltonoise > 10))
    i = random.choice(highstn_index[0])
    read_sdss(cat_file[i], cat_z[i])
    continuum(image_data.lam, image_data.flux)
    index = numpy.where((image_data.lam > 4076) & (image_data.lam < 4130))
    x = image_data.lam[index]
    y = image_data.flux[index] / cont
    n = len(x)                          #the number of data
    mean = sum(x)/n                   #note this correction
    #sigma = sqrt(sum(y*(x-mean)**2)/n) 
    #global popt, perr
    popt, pcov = curve_fit(gaus,x,y,p0=[1,mean,1,0], sigma = (image_data.sigma[index] / cont))
    perr = numpy.sqrt(numpy.diag(pcov))
    #gaussfit(image_data)
    #gaussindex(image_data, 4076, 4130)
    plt.plot(x,y,label='data')
    plt.plot(x,gaus(x,*popt),label='fit',color='red')
    plt.xlabel('Wavelength (angstroms)')
    plt.ylabel('Flux')
    plt.title(cat_file[i])
    High_STN_root = '//Users/nicholashochmuth/Python/Harvard/compact_galaxies/cg_output/High_STN/'
    plt.savefig(High_STN_root + cat_file[i] + '.png', dpi = 300)
    plt.close()
    return popt, perr
    
    