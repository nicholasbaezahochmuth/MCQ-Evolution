from astropy.cosmology import LambdaCDM
import astropy.cosmology
from astropy.io import fits
import numpy as np
import astropy.units as u

cat_ID = cat['BESTOBJID']
EpA = fits.getdata('//Python/EpA_Results.fits')


cosmo = LambdaCDM(H0=70, Om0=0.3, Ode0=0.7)

sb_age_list_gyr=[]
sb_age_list_z = []
zrange = np.arange(0,1396)
for i in zrange:
    age = cosmo.age(cat_z[i])
    age_diff = age.value - (EpA['AGE'][i] / 1000)
    sb_age_list_gyr.append(age_diff * age.unit)
    if age_diff >= 0:
        sb_age_list_z.append(astropy.cosmology.z_at_value(cosmo.age, sb_age_list_gyr[i]))


sb_age_list_z_2 = []
sb_age_list_gyr_2 = []
zrange2 = np.arange(0,26)
for i in zrange2:
    age = cosmo.age(cat_z[high_index[0]][i])
    age_diff = age.value - (EpA['AGE'][high_index[0]][i] / 1000)
    sb_age_list_gyr_2.append(age_diff * age.unit)
    if age_diff >= 0:
        sb_age_list_z_2.append(astropy.cosmology.z_at_value(cosmo.age, sb_age_list_gyr_2[i]))


plt.xlabel(r'$Formation$ $Redshift$', size=16)
plt.ylabel(r'$Frequency$ $(a.u.)$', size=16)
#plt.savefig('//Python/Harvard/SDSSprojectpaper/figures/eps_files/NNNEWW/sb_z_dist2.eps', dpi=1200)


x = sb_age_list_z
q = sb_age_list_z_2
num_bins = 20
range=(0,2.5)
n, bins1= np.histogram(x,num_bins,range) # this is to calculate the number of array elements in the most populated bin; that will be max(n)
m, bins2= np.histogram(q, num_bins, range)

weight_x=np.ones_like(x)/max(n) #every element of the data array is weighted
weight_q=np.ones_like(q)/max(m)

plt.ylim(0,1.2)
plt.xlim(0, 3)
#n, bins1, patches = plt.hist(x,num_bins, range, facecolor='none',weights=weight_x,histtype='stepfilled',hatch='\\\\',edgecolor='black',linewidth=3,label='E+A Sample') #this command actually plots the histogram
#m, bins2, patches = plt.hist(q,num_bins, range, facecolor='none',weights=weight_q,histtype='stepfilled',edgecolor='black',linewidth=3,label='Parent Sample')

plt.hist(x,num_bins, range, facecolor='none',weights=weight_x,histtype='stepfilled',edgecolor='black',linewidth=3,label='Parent Sample')
plt.hist(q,num_bins, range, facecolor='none',weights=weight_q,histtype='stepfilled',hatch='\\\\',linestyle='dashed',edgecolor='black',linewidth=3,label='E+A Sample') #this command actually plots the histogram

plt.legend()
