import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt



EAdata = fits.getdata('//Python/Harvard/cg_output/newsdss_catalogue.fits', 1)
f, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=True, figsize=(14,4))
#high_index = np.where((signaltonoise > 5) & (EAdata['Sigma'][new_cat2] > 5))
#signaltonoise = EAdata['Area'][new_cat2]/EAdata['Area Error'][new_cat2]

x1 = cat_z[high_index[0]]
q1 = cat_z
num_bins = 10
range=(0.1,0.8)
n1, bins= np.histogram(x1,num_bins,range) # this is to calculate the number of array elements in the most populated bin; that will be max(n)
m1, bins= np.histogram(q1,num_bins,range)

weight_x1=np.ones_like(x1)/max(n1) #every element of the data array is weighted
weight_q1=np.ones_like(q1)/max(m1)

ax1.set_ylim(0,1.2)

ax1.hist(q1,num_bins, range, facecolor='none',weights=weight_q1,histtype='stepfilled',edgecolor='black',linewidth=3,label='Parent Sample')
ax1.hist(x1,num_bins, range, facecolor='none',weights=weight_x1,histtype='stepfilled',hatch='\\\\',linestyle='dashed',edgecolor='black',linewidth=3,label='E+A Sample') #this command actually plots the histogram

ax1.set_xlabel(r'$Redshift$', size=16)
ax1.set_ylabel(r'$Frequency$ $(a.u.)$', size=18)
ax1.text(0.15, 1.075, r'$(A)$', fontsize=16)
ax1.set_xticklabels(['',0.2,0.3,0.4,0.5,0.6,0.7,0.8,''])
ax1.legend()





x2 = Sigma_1
q2 = EAdata['Sigma']
num_bins = 10
range=(-1,10)
n2, bins= np.histogram(x2,num_bins,range) # this is to calculate the number of array elements in the most populated bin; that will be max(n)
m2, bins= np.histogram(q2,num_bins,range)

weight_x2=np.ones_like(x2)/max(n2) #every element of the data array is weighted
weight_q2=np.ones_like(q2)/max(m2)

ax2.hist(q2,num_bins, range, facecolor='none',weights=weight_q2,histtype='stepfilled',edgecolor='black',linewidth=3,label='Parent Sample')
ax2.hist(x2,num_bins, range, facecolor='none',weights=weight_x2,histtype='stepfilled',hatch='\\\\',linestyle='dashed',edgecolor='black',linewidth=3,label='E+A Sample') #this command actually plots the histogram

ax2.set_xlabel(r'$H-\delta$ $EW$ $(\AA)$', size=16)
ax2.set_xlim(-2,10)
ax2.text(np.negative(1), 1.075, r'$(B)$', fontsize=16)
ax2.set_xticklabels(['',0,2,4,6,8,''])






x3 = cat['MASS_LP'][high_index[0]]
q3 = cat['MASS_LP']
num_bins = 10
range=(10,12.5)
n3, bins= np.histogram(x3,num_bins,range) # this is to calculate the number of array elements in the most populated bin; that will be max(n)
m3, bins= np.histogram(q3,num_bins,range)

weight_x3=np.ones_like(x3)/max(n3) #every element of the data array is weighted
weight_q3=np.ones_like(q3)/max(m3)

ax3.hist(q3,num_bins, range, facecolor='none',weights=weight_q3,histtype='stepfilled',edgecolor='black',linewidth=3,label='Parent Sample')
ax3.hist(x3,num_bins, range, facecolor='none',weights=weight_x3,histtype='stepfilled',hatch='\\\\',linestyle='dashed',edgecolor='black',linewidth=3,label='E+A Sample') #this command actually plots the histogram

ax3.set_xlim(9.5,12.5)
ax3.set_xlabel(r'$log(M/M_{\odot})$', size=16)
ax3.text(9.75, 1.075, r'$(C)$', fontsize=16)
ax3.set_xticklabels(['',10,10.5,11,11.5,12,''])




f.subplots_adjust(wspace=0)
f.savefig('//Python/Harvard/SDSSProjectPaper/figures/eps_files/3panelhist.eps', dpi=1200)
#f.savefig('//Python/Harvard/SDSSProjectPaper/figures/eps_files/NNNEWW/3panelhist.eps', dpi=1200)
plt.show()

