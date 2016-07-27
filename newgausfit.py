
def g1(x, *p):
    a = p[0]
    x0 = p[1]
    sig = p[2]
    Cons = p[3]
    k = p[4]
    return a*exp(-(x-x0)**2/(2*sig**2))+Cons+(k * x)

import numpy
import warnings

def fitsdss_hdelta2(lam, flux, sigma):
    global y2, sigma2, x1
    index = numpy.where((lam > 4076) & (lam < 4130))
    x1 = lam[index] - 4100
    y1 = flux[index]
    sigma1 = sigma[index]
    n = len(x1)
    mean = sum(x1)/n
    popt_01, pcov_01 = curve_fit(g1,x1,y1,p0=[1,mean,1,0,0], sigma = sigma1)
    perr_01 = np.sqrt(np.diag(pcov_01))
    cont = popt_01[3] + (popt_01[4] * x1)
    y2 = (y1 / cont) - 1
    sigma2 = sigma1 / cont
    global popt, pcov, perr, val, area, area_error
    popt, pcov = curve_fit(gaus,x1,y2,p0=[1,mean,1,0], sigma = sigma2)
    perr = numpy.sqrt(numpy.diag(pcov))
    plt.plot(x1,y2,label='data')
    plt.plot(x1,gaus(x1,*popt),label='fit',color='red')
    plt.xlabel('Wavelength (angstroms)')
    plt.ylabel('Flux')
    plt.show()
    area = numpy.absolute(popt[0]*popt[2]*sqrt(2*numpy.pi)) ## double check "2*pi"
    area_error = area*(sqrt(((perr[0]/popt[0])**2)+((perr[2]/popt[2])**2))) 
    val = [popt, perr, area, area_error]    
    #return area, area_error, popt, perr, val
    print 'Gaussian Area:', area
    print 'Gaussian Area Error:', area_error
    #plt.savefig('~/cg_output/' + title + '.png', dpi = 400)

