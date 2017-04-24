# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 16:05:03 2017

@author: dg144
"""


from pylab import *

sizes = [5, 10, 20, 30, 40, 50, 75, 100, 200, 500]

CVmax = [0.0]*len(sizes)

count = 0

for size in sizes:
    
    
    A = np.load( 'CV' + '_' + str(size) + '.npy')
    
    CVmax[count] = max(A)/(size**2)
    
    count += 1
    
    
#do log plot
plot(sizes,CVmax,color='#7515e1')
plot(sizes,CVmax,'.',color='#1875e1')
#plt.yscale('log')
#plt.xscale('log')
xlabel('n')
ylabel('Cmax/N')

savefig('partb.pdf')