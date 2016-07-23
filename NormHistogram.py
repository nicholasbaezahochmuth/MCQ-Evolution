import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

x = EADN4000
q = SDSSDN4000
num_bins = 30
range=(00.8,2.8)
n, bins1= np.histogram(x,num_bins,range) # this is to calculate the number of array elements in the most populated bin; that will be max(n)
m, bins2= np.histogram(q,num_bins,range)

weight_x=np.ones_like(x)/max(n) #every element of the data array is weighted
weight_q=np.ones_like(q)/max(m)

"""
fig=plt.figure(figsize=(20, 5))
ax1=fig.add_subplot(1,2,1)"""
plt.ylim(0,1.4)
plt.xlim(0.9,2.2)
#n, bins1, patches = plt.hist(x,num_bins, range, facecolor='none',weights=weight_x,histtype='stepfilled',hatch='\\\\',edgecolor='black',linewidth=3,label='E+A Sample') #this command actually plots the histogram
#m, bins2, patches = plt.hist(q,num_bins, range, facecolor='none',weights=weight_q,histtype='stepfilled',edgecolor='black',linewidth=3,label='Parent Sample')

plt.hist(q,num_bins, range, facecolor='none',weights=weight_q,histtype='stepfilled',edgecolor='black',linewidth=3,label='Parent Sample')
plt.hist(x,num_bins, range, facecolor='none',weights=weight_x,histtype='stepfilled',hatch='\\\\',linestyle='dashed',edgecolor='black',linewidth=3,label='E+A Sample') #this command actually plots the histogram

plt.legend(loc = 'upper left')
plt.xlabel(r'$D_{n}4000$',fontsize=16)
plt.ylabel(r'$Frequency$ $(a.u.)$', fontsize=16)
plt.savefig('//Python/Harvard/SDSSProjectPaper/figures/eps_files/NEW_EA_DN4000_HISTOGRAM.eps', dpi = 1200)
#fig.canvas.draw()